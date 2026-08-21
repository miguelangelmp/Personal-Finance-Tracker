import sqlite3

DATABASE_PATH = "data/finance.db"

def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection
