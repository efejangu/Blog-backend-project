from db_engine import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    # fill in with the attributes you suggested
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    posts = relationship("Post", back_populates="user")
    likes = relationship("Likes", back_populates="user")
    comments = relationship("comment", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="posts")
    likes = relationship("Likes", back_populates="post")
    comments = relationship("comment", back_populates="post")

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(DateTime)

    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")

class comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    content = Column(Text)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")