from fastapi import FastAPI
from book_store.api.books.routes import router as books_router
from book_store.api.users.routes import router as users_router

app = FastAPI(title="BookStore")


def register_routers(app: FastAPI):
    app.include_router(users_router, prefix="/api/users", tags=["Users"])
    app.include_router(books_router, prefix="/api/books", tags=["Books"])


register_routers(app)
