from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from flask_login import UserMixin
from db_engine import Base
from datetime import datetime
from sqlalchemy.orm import relationship
import json


def date_string():
    now = datetime.now()
    now_date_string = now.strftime("%m/%d/%Y||%H:%M:%S %p")
    return now_date_string


class User(UserMixin, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

    def __init__(self, email=None, password=None, name=None):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        """
        Creates the string representation of User
        :return: User object
        """
        return '<Checkins %r>' % self.id

    def to_dict(self):
        """
        convert from list to dict
        :return: dict
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class BlogPost(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    img_url = Column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

    def __init__(self, author=None, title=None, subtitle=None, date=None, body=None, img_url=None):
        self.author = author
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.img_url = img_url

    def __repr__(self):
        """
        Creates the string representation of User
        :return: User object
        """
        return '<Checkins %r>' % self.id

    def to_dict(self):
        """
        convert from list to dict
        :return: dict
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("blog_posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    comment_author = relationship("User", back_populates="comments")
    text = Column(Text, nullable=False)

    def __init__(self, parent_post, comment_author, text=None):
        self.parent_post = parent_post
        self.comment_author = comment_author
        self.text = text

    def __repr__(self):
        """
        Creates the string representation of User
        :return: User object
        """
        return '<Checkins %r>' % self.id

    def to_dict(self):
        """
        convert from list to dict
        :return: dict
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
