from pydantic import BaseModel, Field
from typing import Any, Dict, Optional

class JSONInferenceRequest(BaseModel):
    response_schema: Dict[str, Any]
    prompt: str
    context: Optional[str] = Field(default=None, description="Optional context to prepend to the prompt")
