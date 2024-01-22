
import argparse

import time as time
import pandas as pd
from sqlalchemy import create_engine


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))




engine = create_engine('postgresql://root:Vietnam#1@localhost:5432/LOCAL')

df = pd.read_csv('./yellow_tripdata_2023-01.csv', nrows=100)




df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


df_iter = pd.read_csv('./yellow_tripdata_2023-01.csv', iterator=True, chunksize=100000)

df = next(df_iter)

df.to_sql(name = './yellow_taxidata_2023-01', con=engine, if_exists='replace')

df.head(n=0).to_sql(name = './yellow_taxidata_2023-01', con=engine, if_exists='append')


