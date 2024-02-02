import pandas as pd
from time import time
from sqlalchemy import create_engine
import argparse

def main(args):
    user = args.user
    password = args.password
    host =args.host
    port = args.port
    db = args.db
    table_name1 = args.table_name[0]
    table_name2 = args.table_name[1]
    url1 = args.url[0]
    url2 = args.url[1]
    try:
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
        engine.connect()
        print("Connected to DB!")
    except Exception as e:
        print("Could not connect to DB! Try Again")
        print(e)
        exit(0)


    df_iter = pd.read_csv(url1, iterator=True, chunksize=10000)
    df = next(df_iter)
    df.head(n=0).to_sql(name=table_name1, con=engine, if_exists="replace")

    for df in df_iter:
        start_time = time()
        df.lpep_pickup_datetime = pd.to_datetime(df["lpep_pickup_datetime"])
        df.lpep_dropoff_datetime = pd.to_datetime(df["lpep_dropoff_datetime"])
        df.to_sql(name=table_name1, con=engine, if_exists="append")
        end_time = time()
        print(f"inserted another chunk - took time {end_time-start_time}")

    taxi_zone = pd.read_csv(url2)
    taxi_zone.to_sql(name=table_name2, con=engine, if_exists='replace')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV Data from web source into Postgres")
    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host name for postgres db")
    parser.add_argument("--port", help="port number for postgres db")
    parser.add_argument("--db", help="database in which the data needs to stored in postgres")
    parser.add_argument("--table_name", nargs=2, help="table names where the data will be stored")
    parser.add_argument("--url", nargs=2, help="data sources from where data will be extracted")

    args = parser.parse_args()
    main(args)


