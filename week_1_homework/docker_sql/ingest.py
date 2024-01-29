import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = "output.csv"

    os.system(f"wget {url} -O {csv_name}")

    df = pd.read_csv(csv_name)
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
            df.to_sql(con=engine, name=table_name, if_exists="append")
            t_end = time()
            print("inserted another chunk ..., took %.3f second" % (t_end - t_start))
        except:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument('--user', help='user name for Postgres')
    parser.add_argument('--password', help='password for Postgres')
    parser.add_argument('--host', help='host name for Postgres')
    parser.add_argument('--port', help='port number for Postgres')
    parser.add_argument('--db', help='database name for Postgres')
    parser.add_argument('--table_name', help='table name for Postgres')
    parser.add_argument('--url', help='URL of a CSV file')

    args = parser.parse_args()

    main(args)