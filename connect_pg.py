import logging
import psycopg2
from contextlib import contextmanager
from dotenv import dotenv_values

config = dotenv_values('.env')

@contextmanager
def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            user=config['PG_USER'],
            dbname=config['PG_DB'],
            host=config['PG_HOST'],
            password=config['PG_PASSWORD'],
            port=config['PG_PORT']
        )
        yield conn
    except Exception as e:
        logging.error(e)
    finally:
        if conn:
            conn.close()