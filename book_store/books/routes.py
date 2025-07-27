from fastapi import APIRouter
from book_store.books.handlers import router as books_router

router = APIRouter()
router.include_router(books_router)
