import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def get_db_connection():
    """
    Creates a connection to the database.
    We use RealDictCursor so that rows come back as
    {'column': 'value'} instead of (value, value).
    """
    try:
        conn = psycopg2.connect(
            os.getenv("DATABASE_URL"),
            cursor_factory=RealDictCursor
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None