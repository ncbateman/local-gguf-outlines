from fastapi import APIRouter, status
from starlette.responses import JSONResponse
import logging

# Instantiate the router
router = APIRouter()

# Log the instantiation of the router
logging.info("Health check endpoints GET /health and POST /health loaded")

@router.post("/health")
def health_check_post():
    logging.info("Received health check POST request")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "healthy"})

@router.get("/health")
def health_check_get():
    logging.info("Received health check GET request")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "healthy"})
