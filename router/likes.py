#setup api router named likes
#import all the required libraries required for the api router to work
from fastapi import APIRouter, Depends
import db_engine
from sqlalchemy.orm import Session
import schema
from fastapi import HTTPException
from db_engine import get_db



router = APIRouter(
    prefix="/likes",
)
@router.post("/{post_id}")
def like_post(post_id: int , db: Session = Depends(get_db)):
    pass

@router.post("/{post_id}")
def dislike_post(post_id: int , db: Session = Depends(get_db)):
    pass
