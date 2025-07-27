from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from book_store.users.services import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from book_store.users.user_models import User, UserCreate, UserUpdate, MessageResponse
from book_store.core.database import get_db

# TODO: this module looks like part of application layer logic. lets move into application/ folder.
# TODO: I think will be better not create separate router in every module. lets just import it from somewhere.
router = APIRouter()


@router.post("/", response_model=User)
def create_user_endpoint(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)


@router.get("/", response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", response_model=MessageResponse)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
