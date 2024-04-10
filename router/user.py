from fastapi import APIRouter
from repo.user.user import User
import db_engine
from sqlalchemy.orm import Session
from fastapi import Depends
import schema


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

get_db = db_engine.get_db
# create functions and fill them out based on all the methods available in repo.user.user
@router.post("/")
def create_user(user_schema: schema.UserCreate, db: Session = Depends(get_db)):
    user = User(db)
    return user.create_user(user_schema)

@router.get("/")
def get_user_by_email(email, db: Session = Depends(get_db)):
    user = User(db)
    return user.get_user_by_email(email)




