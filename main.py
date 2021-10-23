# import datetime
# import random
import psycopg2
import os
from psycopg2 import Error, connect, sql

os.environ["PGDATABASE"] = 'metrics'
os.environ["PGUSER"] = 'postgres'
os.environ["PGHOST"] = 'localhost'
os.environ["PGPASSWORD"] = 'postgres'
# ENV
pg_dbname = os.environ["PGDATABASE"]
pg_user = os.environ["PGUSER"]
pg_host = os.environ["PGHOST"]
pg_password = os.environ["PGPASSWORD"]

name_coins = ['Dogecoin', 'Crechacoin', 'Sheetcoin']


def PgDb(coin):
    try:
        connect = psycopg2.connect(dbname=pg_dbname,
                                   user=pg_user,
                                   host=pg_host,
                                   password=pg_password)
        cursor = connect.cursor()
        cursor.execute('''
                INSERT INTO rate(coins,created_at, coast, stonks )
                    SELECT  (%(coin)s) as coins,
                            created_at,
                            coast,
                            CASE
                                WHEN coast<3 THEN false
                                WHEN coast>7 THEN true
                                else false
                            END as stonks
                            from(
                                SELECT  created_at,
                                        cast(random() * 10 + 1 as int) as coast
                                        FROM generate_series
                                        ( '2021-01-01'
                                        , '2022-01-01'
                                        , '1 day'::interval) as  created_at
                            ) as d
                ''', {
                    'coin': coin
                })
        connect.commit()
        connect.close()
    except (Exception, Error) as error:
        print("Error: ", error)

for item in name_coins:
    PgDb(item)
