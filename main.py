import psycopg2
import os
import sys
import time
from psycopg2 import Error, connect, sql 

os.environ["PGDATABASE"] = 'metrics'
os.environ["PGUSER"] = 'postgres'
os.environ["PGHOST"] = 'postgres'
# os.environ["PGHOST"] = 'localhost'
os.environ["PGPASSWORD"] = 'postgres'
# ENV
pg_dbname = os.environ["PGDATABASE"]
pg_user = os.environ["PGUSER"]
pg_host = os.environ["PGHOST"]
pg_password = os.environ["PGPASSWORD"]

name_coins = ['Dogecoin', 'Crechacoin', 'Sheetcoin']
cnt_err = 1


def PgDb(coin):
    global cnt_err
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

    except (psycopg2.OperationalError) as error:
        print("Error: ", error, "Sleep 5 seconds.", cnt_err, "try of 5 ")
        time.sleep(5)
        if cnt_err < 5:
            cnt_err += 1
            PgDb(item)
        else:
            sys.exit("Please, you must fix problem described above.")

    except (Error) as error:
        print("Error: ", error)
        print ("Exception TYPE:", type(error))
        connect.close()


for item in name_coins:
    PgDb(item)