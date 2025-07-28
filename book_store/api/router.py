from fastapi import APIRouter, FastAPI
from .users.routes import router as users_router
from .books.routes import router as books_router

api_router = APIRouter()


def register_routers(app: FastAPI):
    api_router.include_router(users_router, prefix="/users", tags=["Users"])
    api_router.include_router(books_router, prefix="/books", tags=["Books"])
    app.include_router(api_router, prefix="/api")
