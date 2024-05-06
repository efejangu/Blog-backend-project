from . import util
from datetime import datetime, timedelta
from jose import jwt
from schema import Token
from fastapi import Depends, HTTPException, status



def create_access_token(subject: dict, expires_delta: int = None) -> dict:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=util.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, "sub": str(subject["id"])}
    encoded_jwt = jwt.encode(to_encode, util.SECRET_KEY, util.ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")

def decode_access_token(token: str):

   try:
        payload = jwt.decode(token, util.SECRET_KEY, algorithms=util.ALGORITHM)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
   except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

   return payload