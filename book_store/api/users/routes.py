from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from book_store.core.database import get_session
from book_store.models.user_models import User, UserCreate, UserUpdate
from book_store.services.users import add_new_user, get_user, list_all_users, modify_user, remove_user

router = APIRouter(tags=["users"])


# TODO: here should be only routes but not routes and handlers
# FIXME: lets try split routes and handlers into different files
@router.post("/", response_model=User)  # <- this is a route decorator
def create_user(user_create: UserCreate, db: Session = Depends(get_session)):  # <- this is a handler function
    return add_new_user(db, user_create)


@router.get("/", response_model=List[User])
def read_users(db: Session = Depends(get_session)):
    return list_all_users(db)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_session)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )  # TODO: lets create custom exception for this instead of using HTTPException directly
    return user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_session)):
    updated_user = modify_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )  # TODO: lets create custom exception for this instead of using HTTPException directly
    return updated_user


@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_session)):
    success = remove_user(db, user_id)
    if not success:
        raise HTTPException(
            status_code=404, detail="User not found"
        )  # TODO: lets create custom exception for this instead of using HTTPException directly
    return {"message": "User deleted successfully"}
