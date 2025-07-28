from typing import List, Optional
from sqlalchemy.orm import Session
from book_store.models.user_models import User, UserCreate, UserUpdate
from book_store.infrastructure.repository_users import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)


def add_new_user(db: Session, user_create: UserCreate) -> User:
    return create_user(db, user_create)


def list_all_users(db: Session) -> List[User]:
    return get_users(db)


def get_user(db: Session, user_id: int) -> Optional[User]:
    return get_user_by_id(db, user_id)


def modify_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    return update_user(db, user_id, user_update)


def remove_user(db: Session, user_id: int) -> bool:
    return delete_user(db, user_id)
