from fastapi import FastAPI
from book_store.users.routes import router as users_router
from book_store.users.domain.database import database

app = FastAPI()
app.include_router(users_router, prefix="/users")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
