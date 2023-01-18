import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(240), nullable=False)
    follows = relationship('Follow', backref='user')
    posts = relationship('Post', backref='user')
    comments = relationship('Comment', backref='user')

class Follow(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship('Comment', backref='post')
    medias = relationship('Media', backref='post')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String())
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(30))
    url = Column(String(240))
    post_id = Column(Integer, ForeignKey('posts.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
