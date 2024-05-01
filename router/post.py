from fastapi import APIRouter
from repo.posts.post import *
import schema
from sqlalchemy.orm import Session
import db_engine
from fastapi import Depends
from fastapi_pagination import Page, Params

router = APIRouter(
    prefix="/post",
    tags=["Post"],
)

get_db = db_engine.get_db
#replace all the return statements in the functions below with pass statements

@router.post("/")
def create_user_post(post_schema: schema.PostCreate, db: Session = Depends(get_db)):
    return create_post( post=post_schema, db=db)

@router.get("/get-posts", response_model=Page[schema.Post])
def get_posts(
        params: Params = Depends(),
        db: Session = Depends(get_db)):

    return paginate_posts(params=params, db=db)


@router.get("/{post_id}")
def get_post(post_id: int,  db: Session = Depends(get_db)):
    return view_post(post_id, db=db)

