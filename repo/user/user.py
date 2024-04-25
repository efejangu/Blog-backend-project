
from sqlalchemy.orm import Session
import models
import schema
from ..auth import util
from fastapi import HTTPException, status

class User:
    def __init__(self, db:Session):
        self.db = db

    def get_user(self, user_id):
        """
        This function retrieves a user based on the provided user_id.
         It queries the database to find the user with the given user_id.
          If the user is not found, it returns an error message. Otherwise,
           it returns the user object.
        """
        user = self.db.query(models.User).filter(user_id == models.User.id).first()
        if user is None:
            return {"error", "user not found"}
        return user

    def create_user(self, user: schema.UserCreate):
        """
        This function handles the POST request to create a new user.
        It takes user_schema of type schema.UserCreate and a database session db, and then creates a new User instance to call the create_user method with the user_schema.
        It returns the result of creating a new user.
        """
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
           return {"detail": "User created successfully", "status": status.HTTP_201_CREATED}


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

