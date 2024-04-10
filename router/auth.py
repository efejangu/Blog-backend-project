from fastapi import APIRouter
import db_engine
import schema
from sqlalchemy.orm import Session
from repo.auth.auth import login_user
from fastapi import Depends

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


get_db = db_engine.get_db
@router.get("/")
def authenticate(login_schema: schema.UserLogin, db: Session = Depends(get_db)):
    login_user(login_schema)
