from sqlalchemy.orm import Session
from app.db.models import UserDB

def create_user(db: Session, name: str, age: int):
    new_user = UserDB(name=name, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
