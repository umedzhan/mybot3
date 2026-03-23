import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = conn.cursor()

def Register(chat_id, first_name):
    sql = "SELECT * FROM users WHERE chat_id = %s"
    cur.execute(sql, (chat_id,))
    result = cur.fetchone()
    if not result:
        sql = "INSERT INTO users (chat_id, first_name) VALUES (%s, %s)"
        cur.execute(sql, (chat_id, first_name))
        conn.commit()

def addUserInfo(chat_id, full_name, phone_number, age, course):
    sql = ("UPDATE users SET "
           "full_name = %s, phone_number = %s, age = %s, course = %s "
           "WHERE chat_id = %s")
    cur.execute(sql, (full_name, phone_number, age, course, chat_id))
    conn.commit()

def getUsers():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()

def countUsers():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]