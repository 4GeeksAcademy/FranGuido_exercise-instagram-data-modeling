import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    _tablename_ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    firstname = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(25), unique=True)
    
class Post(Base):
    _tablename_ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    _tablename_ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(enumerate)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    _tablename_ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id =Column(Integer, ForeignKey('post.id'))


class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
