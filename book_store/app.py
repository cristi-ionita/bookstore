from typing import Union

from fastapi import FastAPI
from users.routes import router as user_router


app = FastAPI()
app.include_router(user_router)

@app.get("/users/me")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
