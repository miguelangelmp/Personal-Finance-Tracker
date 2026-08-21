from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

@dataclass
class Transaction:
    id: int
    type: TransactionType
    amount: Decimal
    category: str
    description: str
    date: date
