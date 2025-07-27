from sqlalchemy.orm import Session
from book_store.core.tables import users
from book_store.users.user_models import User, UserCreate, UserUpdate
from typing import List, Optional
from sqlalchemy import insert, select, update, delete


# TODO: all of the methods relates to infrastructure layer but not to application layer.
# this functions should be moved into infrastructure/repository.py module.
def create_user(db: Session, user_create: UserCreate) -> User:
    user_dict = user_create.dict()
    stmt = insert(users).values(**user_dict)
    result = db.execute(stmt)
    db.commit()
    user_id = result.inserted_primary_key[0]
    return User(id=user_id, **user_dict)


def get_users(db: Session) -> List[User]:
    stmt = select(users)
    result = db.execute(stmt).mappings().all()
    return [User(**row) for row in result]


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    stmt = select(users).where(users.c.id == user_id)
    result = db.execute(stmt).mappings().first()
    if result:
        return User(**result)
    return None


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    existing_user = get_user_by_id(db, user_id)
    if not existing_user:
        return None
    update_data = user_update.dict(exclude_unset=True)
    stmt = update(users).where(users.c.id == user_id).values(**update_data)
    db.execute(stmt)
    db.commit()
    return get_user_by_id(db, user_id)


def delete_user(db: Session, user_id: int) -> bool:
    stmt = delete(users).where(users.c.id == user_id)
    db.execute(stmt)
    db.commit()
    return get_user_by_id(db, user_id) is None
