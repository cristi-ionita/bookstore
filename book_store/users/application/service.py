from typing import List, Optional
from book_store.users.domain.database import database
from book_store.users.domain.user import users, User, UserCreate, UserUpdate
from book_store.users.domain.book import books, Book, BookCreate, BookUpdate


"""USERS"""


async def create_user(user_create: UserCreate) -> User:
    query = users.insert().values(
        username=user_create.username,
        email=user_create.email,
        password=user_create.password  # încă nemodificat hashing
    )
    user_id = await database.execute(query)
    return User(id=user_id, username=user_create.username, email=user_create.email)


async def get_users() -> List[User]:
    query = users.select()
    rows = await database.fetch_all(query)
    return [User(id=row["id"], username=row["username"], email=row["email"]) for row in rows]


async def get_user_by_id(user_id: int) -> Optional[User]:
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user:
        return User(id=user["id"], username=user["username"], email=user["email"])
    return None


async def update_user(user_id: int, user_update: UserUpdate) -> Optional[User]:
    existing_user = await get_user_by_id(user_id)
    if not existing_user:
        return None
    update_data = user_update.dict(exclude_unset=True)
    query = users.update().where(users.c.id == user_id).values(**update_data)
    await database.execute(query)
    return await get_user_by_id(user_id)


async def delete_user(user_id: int) -> bool:
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    user = await get_user_by_id(user_id)
    return user is None

"""BOOKS"""

async def create_book(book_create: BookCreate) -> Book:
    query = books.insert().values(**book_create.dict())
    book_id = await database.execute(query)
    return Book(id=book_id, **book_create.dict())


async def get_books() -> List[Book]:
    query = books.select()
    rows = await database.fetch_all(query)
    return [Book(**row) for row in rows]


async def get_book_by_id(book_id: int) -> Optional[Book]:
    query = books.select().where(books.c.id == book_id)
    book = await database.fetch_one(query)
    return Book(**book) if book else None


async def update_book(book_id: int, book_update: BookUpdate) -> Optional[Book]:
    existing_book = await get_book_by_id(book_id)
    if not existing_book:
        return None
    update_data = book_update.dict(exclude_unset=True)
    query = books.update().where(books.c.id == book_id).values(**update_data)
    await database.execute(query)
    return await get_book_by_id(book_id)


async def delete_book(book_id: int) -> bool:
    query = books.delete().where(books.c.id == book_id)
    await database.execute(query)
    return True
