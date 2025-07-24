from fastapi import FastAPI
from book_store.users.routes import router as users_routes
from book_store.users.domain.database import database

app = FastAPI(
    title="Book Store API",
    description="API pentru gestionarea utilizatorilor și cărților",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users_routes, prefix="/api")
