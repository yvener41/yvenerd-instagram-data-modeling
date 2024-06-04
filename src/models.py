import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250))
    gender = Column(String(250))

    def __repr__(self):
        return '<User> %r' % self.username


class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    icons = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

def __repr__(self):
        return '<Post> %r' % self.title

class Comment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)

def __repr__(self):
        return '<Comment> %r' % self.content

class Reaction(Base):
    __tablename__='reactions'
    id=Column(Integer, primary_key=True)
    number_of_likes = Column(Integer, nullable=False)
    number_of_dislikes = Column(Integer, nullable=False)
    post_id= Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)
    comment_id= Column(Integer, ForeignKey('comments.id'))
    comment = relationship(Comment)

def __repr__(self):
        return '<Reaction> %r' % self.id

class Follower(Base):
    __tablename__='followers'
    id = Column(Integer, primary_key=True)
    #follower_user_id = Column(Integer, ForeignKey('users.id'))
    followed_user_id = Column(Integer, ForeignKey('users.id'))
    #follower = relationship(User)
    followed = relationship(User)


def __repr__(self):
        return '<Follower> %r' % self.id


    








# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
