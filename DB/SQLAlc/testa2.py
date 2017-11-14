# -*- coding: utf-8 -*-

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
#from sqlalchemy.orm import relationship, backref, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Table, Column, String, MetaData 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# configure Session class with desired options
import sqlite3
#import postgresql
#import psycopg2
from sqlalchemy.engine.url import URL

#postgres_db = {'drivername': 'postgres',
#               'username': 'postgres',
#               'password': 'postgres',
#               'host': 'localhost',
#               'port': 5432}
#import pg

#import pg8000


db_string = "postgres://postgres:@localhost:5432/test"

#db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"

db = create_engine(db_string)

meta = MetaData(db)  
film_table = Table('matersjsk1', meta,  
                       Column('title', String),
                       Column('director', String),
                       Column('year', String))

# Create
film_table.create()
insert_statement = film_table.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
conn.execute(insert_statement)