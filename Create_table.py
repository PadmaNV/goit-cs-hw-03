import logging
from psycopg2 import DatabaseError


from connect_pg import connect


def create_table(conn, sql_stmt: str):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_stmt)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        cursor.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE
    );
    """

    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id SERIAL PRIMARY KEY,
     name VARCHAR(50) NOT NULL UNIQUE
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id SERIAL PRIMARY KEY,
     title VARCHAR(100) NOT NULL,
     description TEXT,
     status_id INTEGER NOT NULL,
     user_id INTEGER NOT NULL,     
     FOREIGN KEY (status_id) REFERENCES status(id),
     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """

    try:
        with connect() as conn:
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_status_table)
            create_table(conn, sql_create_tasks_table)
    except RuntimeError as e:
        logging.error(e)