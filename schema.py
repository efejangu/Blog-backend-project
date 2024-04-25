from pydantic import BaseModel
from typing import Union
import datetime

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str

class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str


class UserLogin(BaseModel):
    username: str
    password: str

class PostCreate(BaseModel):
    token: str
    title: str
    content: str

class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: Union[datetime.datetime, None]

class CreateComment(BaseModel):
    access_token: str
    post_id: str
    content: str

class Token(BaseModel):
    access_token: str
    token_type: str