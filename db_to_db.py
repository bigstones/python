import pandas as pd
import psycopg2 as pg
from datetime import datetime
from sqlalchemy import create_engine

send_engine = create_engine('[SQL]://[ID]:[PW]@[HOST]:[PORT]/[DB Name]')

receive_engine = create_engine('[SQL]://[ID]:[PW]@[HOST]:[PORT]/[DB Name]')

"""
PostgreSQL
# import psycopg2
engine = create_engine('postgresql+psycopg2://username:password@host:5432/database')

MySQL
# import pymysql
engine = create_engine('mysql+pymysql://username:password@host:3306/database')

Oracle
# import cx_Oracle
engine = create_engine('oracle://username:password@host:1521/database')
engine = create_engine('oracle+cx_oracle://username:password@host:1521/database')
"""

def SQL_(query):
  connection_ = pg.connect(host='[HOST]', port='[PORT]', dbname='[DB Name]', user='[ID]', password='[PW]')
  
  start_tm = datetime.now()
  print(f'START: {start_tm}')
  query_result = pd.read_sql(query, connction_)
  end_tm = datetime.now()
  print(f'END: {end_tm}')
  print(f'ELAP: {end_tm - start_tm}')
  
  connction_.close()
  return query_result

query_ = 'SELECT * FROM [TABLE]'
data_query = SQL_(query_)
data_query.to_sql('[TABLE]', receive_engine, if_exists='append', index=False)
