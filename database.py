import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


def get_db_connection():
    """
    Creates a connection to the database.
    We use dict_row so that rows come back as
    {'column': 'value'} instead of (value, value).
    """
    try:
        conn = psycopg.connect(
            os.getenv("DATABASE_URL"),
            row_factory=dict_row
        )
        return conn

    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None