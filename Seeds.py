import logging
import random
import psycopg2
from faker import Faker

fake = Faker('uk_UA')
COUNT = 1000


db_config = {
    "dbname": "NVI_database_sql",
    "user": "Padma",
    "password": "Qwerty123",
    "host": "localhost",
}

def generate_users_data(n=COUNT):
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users

def generate_status_data():
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses

def generate_tasks_data(m=COUNT*3):
    tasks = []
    for _ in range(m):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)
        user_id = random.randint(1, COUNT)
        tasks.append((title, description, status_id, user_id))
    return tasks

def populate_db():
    conn = None
    try:
        conn= psycopg2.connect(**db_config)
        cur = conn.cursor()

        users = generate_users_data()
        cur.executemany(sql_insert_users, users)

        status = generate_status_data()
        cur.executemany(sql_insert_status, status)

        tasks = generate_tasks_data()
        cur.executemany(sql_insert_tasks, tasks)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as e:
        logging.error(e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    sql_insert_users = "INSERT INTO users (fullname, email) VALUES (%s, %s);"
    sql_insert_status = "INSERT INTO status (name) VALUES (%s);"
    sql_insert_tasks = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);"

    populate_db()

