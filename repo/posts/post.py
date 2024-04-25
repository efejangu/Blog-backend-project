import models
import schema
from fastapi_pagination import paginate, Params
from fastapi_pagination.links import Page
from sqlalchemy.orm import Session
from ..auth import auth_tokens
from fastapi import HTTPException, status
from datetime import datetime
import models


def create_post(post:schema.PostCreate,db: Session):
    decoded_token = auth_tokens.decode_access_token(post.token)
    new_post = models.Post(
            # save the data from the post schema based on the tables in the database with the same name
        #get the user_id from the decoded token
        user_id = int(decoded_token["sub"]),
        title = post.title,
        content = post.content,
        #set created_at to the current time using datetime module
        created_at = datetime.now()
        )
    db.add(new_post)
    db.commit()
    return {"detail": "Post created successfully", "status": status.HTTP_201_CREATED}
def paginate_posts(params: Params, db: Session) -> Page[schema.Post]:
    stmt = db.query(models.Post).all()
    return paginate(stmt,params=params)
