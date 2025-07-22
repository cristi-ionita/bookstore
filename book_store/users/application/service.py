from typing import List
from book_store.users.domain.database import database
from book_store.users.domain.user import users, User


async def create_user(user: User):
    query = users.insert().values(
        username=user.username,
        email=user.email,
        password=user.password  # hashing
    )
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}


async def get_users() -> List[User]:
    query = users.select()
    rows = await database.fetch_all(query)
    return [User(**row) for row in rows]
