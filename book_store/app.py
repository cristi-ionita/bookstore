from fastapi import FastAPI
from book_store.books.routes import router as books_router
from book_store.users.routes import router as users_router


app = FastAPI(title="BookStore")

# TODO: this looks like code dublication (difference only in arguments). lets create a function to register routers
app.include_router(users_router, prefix="/api/users")
app.include_router(books_router, prefix="/api/books")
