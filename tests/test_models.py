from datetime import date
from src.models import Transaction, TransactionType


def test_create_transaction():
    transaction = Transaction(
        id=1,
        type=TransactionType.EXPENSE,
        amount=25.50,
        category="Food",
        description="Wendys",
        date=date.today()
    )

    assert transaction.id == 1
    assert transaction.type == TransactionType.EXPENSE
    assert transaction.amount == 25.50
    assert transaction.category == "Food"
    assert transaction.description == "Wendys"