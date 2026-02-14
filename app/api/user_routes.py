from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.user_crud import create_user
from app.db.database import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.age)
