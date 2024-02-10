from fastapi import APIRouter, status, Body, HTTPException
from starlette.responses import JSONResponse
from ctransformers import AutoModelForCausalLM
import torch
from transformers import PretrainedConfig
from outlines.models.transformers import Transformer, TransformerTokenizer
import outlines.text.generate as generate
from src.inference.model import Model
from src.schema.json_inference_request import JSONInferenceRequest
from pydantic import BaseModel, create_model
from typing import Any, Dict
import json  # Use the built-in JSON library
import logging

# Initialize the model and tokenizer
logging.info("Loading inference model")
llm = AutoModelForCausalLM.from_pretrained("/app/models/model", model_file="miqu-1-70b.q2_K.gguf", model_type='llama')
model = Model(PretrainedConfig(), llm)
logging.info("Loading inference tokenizer")
tokenizer = TransformerTokenizer("/app/models/tokenizer")
transformer_model = Transformer(model=model, tokenizer=tokenizer)

router = APIRouter()

# Log the instantiation of the router and model loading
logging.info("JSON inference router loaded")

@router.post("/json_inference")
async def json_inference_post(request: dict = Body(...)):  # Accept a raw dict
    logging.info("Received JSON inference request")

    # Extract the schema and prompt directly from the request
    schema = request.get("response_schema")  # This should be a JSON schema string or dict
    prompt = request.get("prompt", "")
    context = request.get("context", "")

    # Construct the prompt with optional context
    full_prompt = f"###CONTEXT\n{context}\n###PROMPT\n{prompt}" if context else prompt
    
    logging.info(f"Generating response for prompt: {full_prompt[:50]}...")  # Log the beginning of the prompt for brevity

    # Use the schema directly with generate.json
    try:
        # If your schema is a dict, convert it to a string. If it's already a string, use it as is.
        schema_str = json.dumps(schema) if isinstance(schema, dict) else schema
        answer = generate.json(transformer_model, schema_str)(full_prompt)
    except Exception as e:
        logging.error(f"Error during generation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error during generation: {str(e)}")

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"response": answer}
    )