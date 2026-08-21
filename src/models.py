from dataclasses import dataclass
from datetime import date
from enum import Enum

class transactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

@dataclass
class Transaction:
    id: int
    type: transactionType
    ammount: float
    category: str
    description: str
    date: date


# test transaction
transaction = Transaction(
    id=1,
    type = transactionType.EXPENSE,
    ammount = 25.50,
    category = "Food",
    description = "Wendys",
    date = date.today()
)

print(transaction)