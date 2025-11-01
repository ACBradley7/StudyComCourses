import sys
import sqlite3
import re

def db_connection():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, grade INTEGER, email TEXT)")
    conn.commit()
    
    return cursor, conn

def close_conn(conn):
    conn.close()

def welcome():
    print("\nWelcome to the student database management module.")

def menu(cursor, conn):
    print("\nYour choices are (a)dd record, (v)iew all, (u)pdate record, (d)elete record, (q)uit.")

    while True:
        choice = input("\n(a)dd, (v)iew, (u)pdate, (d)elete, (q)uit: ")
        choice = choice.lower()

        if (is_menu_choice_valid(choice)):
            do_operation(choice, cursor, conn)
        elif choice == "":
            print("\nQuitting...")
            break
        else:
            print("Please eneter a, v, u, d, or q...")

def is_menu_choice_valid(choice):
    if (choice == "a" or choice == "add"
        or choice == "v" or choice == "view"
        or choice == "u" or choice == "update"
        or choice == "d" or choice == "delete"
        or choice == "q" or choice == "quit"
        ):
        return True
    else:
        return False

def do_operation(choice, cursor, conn):
    match choice:
        case "a" | "add":
            add_record(cursor, conn)
        case "v" | "view":
            view_records(cursor)
        case "u" | "update":
            update_record(cursor, conn)
        case "d" | "delete":
            delete_record(cursor, conn)
        case "q" | "quit":
            quit_func()

def get_name():
    while True:
        name = input("\nStudent Name: ")

        if re.match(r"^(?! )[A-Za-z]+(?: [A-Za-z]+)*(?<! )$", name):
            print("\nValid name...")
            break
        elif name == "":
            break
        else:
            print("\nEnter only letters with a maximum of one space in-between the letters...")

    return name

def get_grade():
    while True:
        grade = input("\nStudent Grade: ")

        if re.match(r"^\d+$", grade):
            print("\nValid grade...")
            break
        elif grade == "":
            break
        else:
            print("\nEnter only an integer...")

    return grade

def get_email():
    while True:
        email = input("\nStudent Email: ")

        if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
            print("\nValid email...")
            break
        elif email == "":
            break
        else:
            print("\nEnter a valid email address with an @ symbol and a valid domain name with a dot symbol...")

    return email

def add_record(cursor, conn):
    name = get_name()
    if name == "": print("No record added..."); return

    grade = get_grade()
    if grade == "": print("No record added..."); return

    email = get_email()
    if email == "": print("No record added..."); return

    try: 
        cursor.execute("INSERT INTO students (name, grade, email) VALUES (?, ?, ?)", (name, grade, email))
        conn.commit()
        print("\nStudent record added...")
    except sqlite3.Error as e:
        print(f"Error adding record: {e}")

def view_records(cursor):
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    disp_records(records)

def disp_records(records):
    if (len(records) == 0):
        print("\nNo records to view...")

    for record in records:
        print(f"\nID: {record[0]} , Name: {record[1]} , Grade: {record[2]} , Email: {record[3]}")

def update_record(cursor, conn):
    while True:
        record_id = input("\nRecord ID: ")

        if re.match(r"^\d+$", record_id):
            if (check_record_exists(cursor, record_id)):
                change_record(cursor, conn, record_id)
                break
            else:
                break
        elif record_id == "":
            break
        else:
            print("\nEnter a valid integer for the student id...")

def check_record_exists(cursor, id):
    cursor.execute(f"SELECT exists(SELECT 1 FROM students WHERE id = {id}) AS row_exists;")
    exists = cursor.fetchone()[0]

    if exists:
        return True
    else:
        print("\nStudent record does not exist...")
        return False
    
def change_record(cursor, conn, id):
    record = disp_record(cursor, id)

    while True:
        choice = input("\nAdjust (n)ame, (g)rade, (e)mail: ")
        choice = choice.lower()

        if (is_adjustment_choice_valid(choice)):
            do_adjustment(choice, record, cursor, conn)
            break
        elif choice == "":
            break
        else:
            print("\nInput n, g, or e...")

def disp_record(cursor, id):
    cursor.execute(f"SELECT * FROM students WHERE id = {id};")
    record = cursor.fetchone()
    print(f"\nCurrent student... ID: {record[0]} , Name: {record[1]} , Grade: {record[2]} , Email: {record[3]}")
    return record

def is_adjustment_choice_valid(choice):
    if (choice == "n" or choice == "name"
        or choice == "g" or choice == "grade"
        or choice == "e" or choice == "email"
        ):
        return True
    else:
        return False

def do_adjustment(choice, record, cursor, conn):
    match choice:
        case "n" | "name":
            col = "name"
            val = get_name()
        case "g" | "grade":
            col = "grade"
            val = get_grade()
        case "e" | "email":
            col = "email"
            val = get_email()
    
    if val == "":
        print("No adjustments made...")
        return

    update_table(record[0], col, val, cursor, conn)

def update_table(id, col, val, cursor, conn):
    try:
        cursor.execute(f"UPDATE students SET '{col}' = '{val}' WHERE id = {id};")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

    conn.commit()

def delete_record(cursor, conn):
    while True:
        record_id = input("\nRecord ID: ")

        if re.match(r"^\d+$", record_id):
            if (check_record_exists(cursor, record_id)):
                del_record(cursor, conn, record_id)
                break
            else:
                break
        elif record_id == "":
            print("\nNo record deleted...")
            break
        else:
            print("\nEnter a valid integer for the student id...")

def del_record(cursor, conn, id):
    record = disp_record(cursor, id)

    if (confirm_deletion(id)):
        del_record_from_db(cursor, conn, record)
        print("\nRecord deleted...")
    else:
        print("\nNo record deleted...")

def confirm_deletion(id):
    print(f"\nConfirming deletion for record {id}...")

    choice = input("(y)es/(n)o: ")
    choice = choice.lower()

    if choice == "y" or choice == "yes":
        return True
    else:
        return False

def del_record_from_db(cursor, conn, record):
    cursor.execute(f"DELETE FROM students WHERE id = {record[0]};")
    conn.commit()

def quit_func():
    print("\nQuitting...")
    sys.exit()

def main():
    cursor, conn = db_connection()

    welcome()
    menu(cursor, conn)
    
    close_conn(conn)

main()