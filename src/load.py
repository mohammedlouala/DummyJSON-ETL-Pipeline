import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = (
    f'postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

engine = create_engine(DATABASE_URL)

def load_to_postgres(df, table_name):

    df.to_sql(table_name,
        engine,
        schema = 'silver',
        if_exists = 'replace',
        index = False
    )

    print(f"{table_name} load to postgres successfully")
