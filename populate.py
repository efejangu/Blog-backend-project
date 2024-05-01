#write me a database population script to add users and post to the database using Faker python

from faker import Faker
from sqlalchemy.orm import Session
import models
import db_engine
from repo.auth import util

#create a faker instance
fake = Faker()

#create a session
session = Session(db_engine.engine)

#create 50 users using a for loop inside a  function called create users
def create_users():
    #create a try statement to catch any errors
    try:
        user = None
        for _ in range(50):
            user = models.User(
                username = fake.user_name(),
                email = fake.email(),
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                hashed_password = util.get_hashed_password(fake.password())
            )
            session.add(user)
            session.commit()


    except Exception as e:
        print ("Could not create users\n Reason:", e)

#Do the same for a new function called create_posts

def create_posts():
    try:
        post = None
        for _ in range(50):
            post = models.Post(
                title = fake.sentence(),
                content = fake.text(),
                user_id = 1,
                created_at = fake.date_time()
            )
            session.add(post)
            session.commit()

    except Exception as e:
        print ("Could not create posts\n Reason:", e)



if __name__ == "__main__":
   # create_users()
    create_posts()

print("user_count: ",session.query(models.User).count())
print("Post_count: ",session.query(models.Post).count())
