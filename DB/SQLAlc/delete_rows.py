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
conn = engine.connect()

meta = MetaData(engine, reflect=True)
user_t = meta.tables['user']

# select * from user_t
sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res: print (_row)

# delete l_name == 'Hello'
del_st = user_t.delete().where(
      user_t.c.l_name == 'Hello')
print ('----- delete -----')
res = conn.execute(del_st)