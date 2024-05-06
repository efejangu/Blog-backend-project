#setup api router named likes
#import all the required libraries required for the api router to work
from fastapi import APIRouter, Depends
import db_engine
from sqlalchemy.orm import Session
import schema
from fastapi import HTTPException
from repo.posts.likes import  like_post, dislike_post
from db_engine import get_db



router = APIRouter(
    prefix="/likes",
    tags=["likes"]
)
@router.post("/like-post/{token}/{post_id}")
def like_user_post(token: str, post_id: int , db: Session = Depends(get_db)):
    return like_post(token,post_id, db)


@router.post("/dislike-post/{token}/{post_id}")
def dislike_user_post(token: str, post_id: int, db: Session = Depends(get_db)):
    return dislike_post(token, post_id, db)