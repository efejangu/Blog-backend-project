import models
import schema
from sqlalchemy.orm import Session
from ..auth.auth_tokens import decode_access_token
from fastapi import HTTPException, status
import datetime

def create_comment(comment: schema.CreateComment, db: Session,):
    decoded_token = decode_access_token(comment.access_token)
    new_comment = models.comment(
        user_id = int(decoded_token["sub"]),
        post_id = comment.post_id,
        content = comment.content,
        created_at = datetime.datetime.now()
    )
    db.add(new_comment)
    db.commit()
    return {"detail": "Comment created successfully", "status": status.HTTP_201_CREATED}

def delete_comment(comment_id: int, db: Session):
    pass
    #TODO


def edit_comment(db: Session, updated_comment: schema.UpdateComment):
    user_token = decode_access_token(updated_comment.access_token)
    #check if comment exists
    original_comment = db.query(models.comment).filter((updated_comment.post_id == models.comment.id) and (models.comment.user_id == int(user_token["sub"]))).first()
    if original_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    original_comment.content = updated_comment.content
    db.commit()
    return {"detail": "Comment updated successfully", "status": status.HTTP_200_OK}
