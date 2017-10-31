# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, String, Integer

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

from sqlalchemy import inspect

db_uri = 'sqlite:///db.db'
#db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

con = engine.connect() 

trans = con.begin() 

for name, table in meta.tables.items(): 

    print (table.delete() )
    con.execute(table.delete()) 

trans.commit() 