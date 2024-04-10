from pydantic import BaseModel

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
    user_id: int
    title: str
    content: str

class Token(BaseModel):
    access_token: str
    token_type: str