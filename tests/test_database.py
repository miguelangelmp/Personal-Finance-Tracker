from datetime import date

from src.database import (
    create_connection, 
    create_transactions_table, 
    add_transaction,
    get_transactions, 
    delete_transaction
)
from src.models import Transaction, TransactionType


def test_add_transaction():
    connection = create_connection(":memory:")
    create_transactions_table(connection)

    transaction = Transaction(
        id=1,
        type=TransactionType.EXPENSE,
        amount=25.50,
        category="Food",
        description="Wendys",
        date=date.today()
    )

    add_transaction(connection, transaction)
    transactions = get_transactions(connection)

    assert len(transactions) == 1
    assert transactions[0].type == TransactionType.EXPENSE
    assert transactions[0].amount == 25.50
    assert transactions[0].category == "Food"
    assert transactions[0].description == "Wendys"

    connection.close()

def test_delete_transaction():
    connection = create_connection(":memory:")
    create_transactions_table(connection)

    transaction = Transaction(
        id=1,
        type=TransactionType.EXPENSE,
        amount=25.50,
        category="Food",
        description="Wendys",
        date=date.today()
    )

    add_transaction(connection, transaction)
    delete_transaction(connection, 1)
    transactions = get_transactions(connection)

    assert len(transactions) == 0

    connection.close()