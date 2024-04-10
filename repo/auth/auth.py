import schema
from sqlalchemy.orm import Session
import models
from . import util
from fastapi import HTTPException, status
from . import auth_tokens

def authenticate_user(user:schema.UserLogin, db:Session):
    """
    A function to authenticate a user based on the provided user login information.

    Parameters:
    - user: an instance of schema.UserLogin containing the user's login information.
    - db: a Session object representing the database session.

    Returns:
    - False if the user is not found or the password is incorrect.
    - A dictionary with the user's id and username if authentication is successful.
    """
    attempting_user = db.query(models.User).filter(user.username ==models.User.username ).first()
    if attempting_user is None:
        return False
    if util.verify_password(user.password, attempting_user.hashed_password):
        return {"id": attempting_user.id, "username": attempting_user.username}


def login_user(user_schema:schema.UserLogin, db:Session):
    auth_user = authenticate_user(user_schema)
    if auth_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")


    return schema.Token(
        access_token = auth_tokens.create_access_token(auth_user),
        token_type = "bearer"
    ).dict()

