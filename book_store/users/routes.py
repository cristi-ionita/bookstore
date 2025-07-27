from fastapi import APIRouter
from book_store.users.handlers import router as user_router

router = APIRouter()
router.include_router(user_router)
