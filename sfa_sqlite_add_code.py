# /// script
# dependencies = [
#   "sqlite3",
#   "os",
#   "argparse",
#   "uuid",
# ]
# ///

import sqlite3
import os
import argparse
import uuid

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PythonCode (
        id TEXT PRIMARY KEY,
        filename TEXT,
        code TEXT
    )
    ''')
    conn.commit()

def add_code_to_db(conn, directory):
    cursor = conn.cursor()
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            with open(os.path.join(directory, filename), 'r') as file:
                code = file.read()
                cursor.execute('''
                INSERT INTO PythonCode (id, filename, code)
                VALUES (?, ?, ?)
                ''', (str(uuid.uuid4()), filename, code))
    conn.commit()

def main():
    parser = argparse.ArgumentParser(description="Add Python code to SQLite database")
    parser.add_argument('-d', '--db', required=True, help="Path to SQLite database file")
    parser.add_argument('-p', '--path', required=True, help="Path to directory containing Python files")
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    create_table(conn)
    add_code_to_db(conn, args.path)
    conn.close()

if __name__ == "__main__":
    main()
