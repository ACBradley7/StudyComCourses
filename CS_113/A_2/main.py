import sqlite3

def db_connection():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER, email TEXT)")
    cursor.execute("INSERT INTO students (name, grade, email) VALUES ('Tobias', 10, 'tobiasJ@gmail.com')")
    conn.commit()
    
    return cursor, conn

def get_data(cursor):
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchone()
    print(f"id: {result[0]}, name: {result[1]}, grade: {result[2]}, email: {result[3]}")

def close_conn(conn):
    conn.close()

def main():
    cursor, conn = db_connection()
    get_data(cursor)
    close_conn(conn)

main()