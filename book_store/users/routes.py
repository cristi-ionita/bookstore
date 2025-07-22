from fastapi import APIRouter
from book_store.users.application.handlers import router as users_router

router = APIRouter()
router.include_router(users_router)
