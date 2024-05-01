
from sqlalchemy.orm import Session
import models
from ..auth.auth_tokens import decode_access_token

def did_user_like_post(user_id:int, post_id, db:Session):

    like_info = db.query(models.Likes).filter(models.Likes.post_id == post_id).first()
    if like_info is None:# if like doesn't exist
        return False
    else:
        # if like exists, check if user has liked the post before, if so return True
        lookup_user_like = db.query(models.LookUp).filter(models.LookUp.user_id == user_id,
                                                          models.LookUp.like_id == like_info.id).first()
        if lookup_user_like.like_status == "Like":
            return True


def like_post(token:str, post_int, db:Session):
    user = decode_access_token(token)
    user = int(user.get("sub"))
    if did_user_like_post(user, post_int, db):
        return
    else:
        pass
    



def dislike_post(post_int, db:Session):
    pass