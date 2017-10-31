# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
     __tablename__   = 'user'
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(50))

stmt = User.__table__.update().where(User.id==5).values(name='user #5')

     def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///tdb.db')
Base.metadata.create_all(engine)