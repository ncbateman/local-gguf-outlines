from fastapi import APIRouter
from .json_inference import router as json_inference_router
from .health import router as health_router

router = APIRouter()
router.include_router(json_inference_router)
router.include_router(health_router)
