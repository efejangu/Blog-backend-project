from fastapi import APIRouter
import db_engine
import schema
from sqlalchemy.orm import Session
#import auth.py file from repo/auth
from repo.auth import auth
from fastapi import Depends

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


get_db = db_engine.get_db
@router.post("/login")
def login(login_schema: schema.UserLogin, db: Session = Depends(get_db)):
    return auth.login_user(login_schema, db)

