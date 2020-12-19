from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from crud import Session

Base = declarative_base()

creators = Table('creators', Base.metadata,
                 Column('movie_id', Integer, ForeignKey('movies.id')),
                 Column('studio_id', Integer, ForeignKey('studios.id')))

casts = Table('casts', Base.metadata,
              Column('movie_id', Integer, ForeignKey('movies.id')),
              Column('actor_id', Integer, ForeignKey('actors.id')))


class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    studio_id = Column(Integer, ForeignKey('studios.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))
    studio = relationship("Studio")


class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    contracts = relationship("Contract")


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    description = Column(String)
    budget = Column(Integer)
    cast = relationship("Actor", secondary=casts, lazy='subquery')


class Studio(Base):
    __tablename__ = 'studios'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    movies = relationship("Movie", secondary=creators, lazy='subquery')

