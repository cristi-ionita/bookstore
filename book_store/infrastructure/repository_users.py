from typing import List, Optional

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from book_store.core.tables.user_tables import users
from book_store.models.user_models import User, UserCreate, UserUpdate


# Lets create AbstractRepository and BaseRepository classes to handle common CRUD operations to avoid code duplication
# and boilerplate code.
# TODO: lets move these methods into some kind of service class UsersRepository
def create_user(db: Session, user_create: UserCreate) -> User:
    insert_stmt = users.insert().values(
        username=user_create.username,
        email=user_create.email,
        full_name=user_create.full_name,
        password=user_create.password,
    )
    result = db.execute(insert_stmt)
    db.commit()
    user_id = result.inserted_primary_key[0]
    user = get_user_by_id(db, user_id)
    if user is None:
        raise Exception("User not found after creation")
    return user


def get_users(db: Session) -> List[User]:
    stmt = select(users)
    result = db.execute(stmt).fetchall()
    return [User(**row._mapping) for row in result]


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    stmt = users.select().where(users.c.id == user_id)
    result = db.execute(stmt).first()
    if result is None:
        return None
    return User(**result._mapping)


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    update_data = user_update.model_dump(exclude_unset=True)
    if not update_data:
        return get_user_by_id(db, user_id)
    query = users.update().where(users.c.id == user_id).values(**update_data)
    result = db.execute(query)
    db.commit()
    if result.rowcount == 0:
        return None
    return get_user_by_id(db, user_id)


def delete_user(db: Session, user_id: int) -> bool:
    stmt = delete(users).where(users.c.id == user_id)
    result = db.execute(stmt)
    db.commit()
    return result.rowcount > 0
