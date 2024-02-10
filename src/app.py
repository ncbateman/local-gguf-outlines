from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router
from src.utils.logger import setup_logging
import logging

# Set up logging for the application
setup_logging()

# Create the FastAPI app instance
app = FastAPI(title="Local GGUF Outlines", version="1.0")
logging.info(f"{app.title} v{app.version} is starting up...")

# Configure CORS settings as lists for better control and readability
origins = ["*"]  # This should be more restrictive in production
allow_methods = ["*"]  # Consider specifying only the methods your application uses
allow_headers = ["*"]  # Specify only the headers needed by your application

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

# Log warnings for potentially insecure CORS configuration
if "*" in origins:
    logging.warning("CORS is configured to allow all origins. This is strongly not recommended in production environments.")

if "*" in allow_methods:
    logging.warning("CORS is configured to allow all methods. This is strongly not recommended in production environments.")

if "*" in allow_headers:
    logging.warning("CORS is configured to allow all headers. This is strongly not recommended in production environments.")

# Include the routers from the routes package
logging.info("Including application routers...")
app.include_router(router)
