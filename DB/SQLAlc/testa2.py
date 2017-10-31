# -*- coding: utf-8 -*-

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
#from sqlalchemy.orm import relationship, backref, user
from sqlalchemy.ext.declarative import declarative_base
 
 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# configure Session class with desired options
import sqlite3


# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('db.db')

db.close()