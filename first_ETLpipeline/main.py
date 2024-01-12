"""
Python Extract Transform Load Example
"""

# %%
import requests
import pandas as pd
from sqlalchemy import create_engine

def extract()-> dict:
    """ This API extracts data from
    http://universities.hipolabs.com
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

def transform(data:dict) -> pd.DataFrame:
    """ Transforms the dataset into desired structure and filters"""
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API {len(data)}")
    df = df[df["name"].str.contains("Iowa")]
    print(f"Number of universities in Iowa {len(df)}")
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    return df[["domains","country","web_pages","name"]]

def load_to_mysql(df: pd.DataFrame) -> None:
    """ Loads data into a MySQL database named 'test' """
    # Replace 'username' and 'password' with your MySQL credentials
    mysql_username = 'root'
    mysql_password = 'Vietnam#1'
    mysql_host = 'localhost'  # Change the host if your MySQL server is on a different machine
    mysql_database = 'test'

    # Create the MySQL connection string
    mysql_connection_str = f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_database}'

    # Create the SQLAlchemy engine
    mysql_engine = create_engine(mysql_connection_str)

    # Load the DataFrame into the 'cal_uni' table in the MySQL database
    df.to_sql('Iowa_College', mysql_engine, if_exists='replace', index=False)

# Example usage:
# Assuming you have a DataFrame called 'your_dataframe'
# load_to_mysql(your_dataframe)

# %%
data = extract()
df = transform(data)
load_to_mysql(df)