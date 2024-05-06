
from sqlalchemy.orm import Session
import models
from ..auth.auth_tokens import decode_access_token


def did_user_like_post(user_id:int, post_id, db:Session):
    like_info = db.query(models.Likes).filter(models.Likes.post_id == post_id).first()
    if like_info is None:# if like doesn't exist
        return False
    else:
        # if like exists, check if user has liked the post before, if so return True
        lookup_user_like = db.query(models.LookUp).filter(models.LookUp.user_id == user_id, models.LookUp.post_id == like_info.post_id).first()
        if lookup_user_like.like_status == "Like":
            return True


def did_user_dislike_post(user_id:int, post_id, db:Session):
    dislike_info = db.query(models.Likes).filter(models.Likes.post_id == post_id).first()
    if dislike_info is None:
        return False
    else:
        lookup_user_like = db.query(models.LookUp).filter(models.LookUp.user_id == user_id,models.LookUp.post_id == dislike_info.post_id).first()
        if lookup_user_like.like_status == "Dislike":
            return True

def like_post(token:str, post_int, db:Session):
    user = decode_access_token(token)
    user = int(user.get("sub"))
    if did_user_like_post(user, post_int, db):
        return{"detail": "Post already liked"}
    else:
        # if the user hasn't liked the post before
        #we check if the post has been disliked
        # if so, we remove the dislike and create a new like
        if did_user_dislike_post(user, post_int, db):
            removed_dislike = db.query(models.Likes).filter(models.Likes.post_id == post_int).first()
            removed_dislike.dislike_count -= 1
            db.add(removed_dislike)
            db.commit()

        updated_lookup_table = models.LookUp(user_id=user, post_id=post_int, like_status="Like")
        new_like = models.Likes(post_id=post_int)
        new_like.like_count =+ 1
        db.add(updated_lookup_table)
        db.add(new_like)
        db.commit()
        return {"like_count": new_like.like_count, "dislike_count": new_like.dislike_count}


def dislike_post(token:str, post_int, db:Session):
    user = decode_access_token(token)
    user = int(user.get("sub"))
    if did_user_dislike_post(user, post_int, db):
        return
    else:
        # if the user hasn't disliked the post before
        #we check if the post has been liked
        # if so, we remove the like and create a new dislike
        if did_user_like_post(user, post_int, db):
            removed_like = db.query(models.Likes).filter(models.Likes.post_id == post_int).first()
            removed_like.like_count -= 1
            db.add(removed_like)
            db.commit()

        updated_lookup_table = models.LookUp(user_id=user, post_id=post_int, like_status="Dislike")
        new_dislike = models.Likes(post_id=post_int)
        new_dislike.dislike_count =+ 1
        db.add(updated_lookup_table)
        db.add(new_dislike)
        db.commit()

        return {"like_count": new_dislike.like_count, "dislike_count": new_dislike.dislike_count}