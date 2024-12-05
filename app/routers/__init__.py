from fastapi import APIRouter

from .message import router_message

router = APIRouter()
router.include_router(router_message)

__all__ = ["router"]