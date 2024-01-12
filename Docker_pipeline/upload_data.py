
import pandas as pd
from sqlalchemy import create_engine



df = pd.read_csv('./yellow_tripdata_2023-01.csv', nrows=100)





engine = create_engine('postgresql://root:Vietnam#1@localhost:5432/LOCAL')
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


df_iter = pd.read_csv('./yellow_tripdata_2023-01.csv', iterator=True, chunksize=100000)

df = next(df_iter)

df.to_sql(name = './yellow_taxidata_2023-01', con=engine, if_exists='replace')

df.head(n=0).to_sql(name = './yellow_taxidata_2023-01', con=engine, if_exists='append')


