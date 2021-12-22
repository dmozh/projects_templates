from fastapi import APIRouter

from .healthcheck import router as health_check_router

router = APIRouter()
router.include_router(health_check_router)