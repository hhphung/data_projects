from sqlalchemy import create_engine
import pandas as pd
import psycopg2

engine = create_engine('postgresql://root:Vietnam#1@localhost:5432/LOCAL')

engine.connect()


df = pd.read_csv('yellow_tripdata_2023-01.csv', nrows=100)

df