import sqlite3

DATABASE_PATH = "data/finance.db"

def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_transactions_table(connection):
    sql = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    """

    connection.execute(sql)
    connection.commit()

