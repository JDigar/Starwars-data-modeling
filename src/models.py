import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

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




class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    age = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    favorites = relationship('Favorites', backref='user', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(String(120), nullable=False)
    rotation = Column(String(120), nullable=False)  
    diameter = Column(String(120), nullable=False)   
    favorites = relationship('Favorites', backref='planets', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    gender = Column(String(120), nullable=False)
    height = Column(String(120), nullable=False)  
    eye_color = Column(String(120), nullable=False)   
    favoritos = relationship('Favoritos', backref='characters', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    manufacturer = Column(String(120), nullable=False)  
    Cost_in_credits = Column(String(120), nullable=False)   
    favoritos = relationship('Favoritos', backref='vehicles', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)
    charancteres_id = Column(Integer, ForeignKey('characters.id'),
        nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'),
        nullable=False)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')