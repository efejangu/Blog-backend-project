
from sqlalchemy.orm import Session
import models
import schema
from ..auth import util

class User:
    def __init__(self, db:Session):
        self.db = db

    def get_user(self, user_id):
        user = self.db.query(models.User).filter(user_id == models.User.id).first()
        if user is None:
            return {"error", "user not found"}
        return user

    def create_user(self, user: schema.UserCreate):
       #check if user email exists before adding the user into the table
        existing_user = self.db.query(models.User).filter(user.email == models.User.email).first()
        if existing_user is not None:
            return {"error", "user already exists"}
        else:
           potential_user = models.User(
               username = user.username,
               email = user.email,
               first_name = user.first_name,
               last_name = user.last_name,
               hashed_password = util.get_hashed_password(user.password)
           )

           self.db.add(potential_user)
           self.db.commit()

    def get_user_by_email(self, email):
        user = self.db.query(models.User).filter(email == models.User.email).first()
        if user is None:
            return {"error", "user not found"}

        returned_user = schema.User(
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            email =  user.email
        )
        return returned_user.dict()

