import sqlite3

from src.models import Transaction, TransactionType
from datetime import date

DATABASE_PATH = "data/finance.db"

def create_connection(database_path=DATABASE_PATH):
    connection = sqlite3.connect(database_path)
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

def add_transaction(connection, transaction):
    sql = """
    INSERT INTO transactions
    (type, amount, category, description, date)
    VALUES (?, ?, ?, ?, ?);
    """

    connection.execute(
    sql,
    (
        transaction.type.value,
        transaction.amount,
        transaction.category,
        transaction.description,
        transaction.date.isoformat()
    )
)
    connection.commit()

def get_transactions(connection):
    sql = """
    SELECT id, type, amount, category, description, date
    FROM transactions
    """

    cursor = connection.execute(sql)
    rows = cursor.fetchall()

    transactions = []

    for row in rows:
        transaction = Transaction(
            id = row[0],
            type = TransactionType(row[1]),
            amount = row[2],
            category = row[3],
            description = row[4],
            date = date.fromisoformat(row[5])
        )
        transactions.append(transaction)
        
    return transactions
