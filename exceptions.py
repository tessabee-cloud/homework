class FinanceError(Exception):
    """Base exception for the finance tracker."""
    pass


class InvalidAmountError(FinanceError):
    pass


class InvalidDateError(FinanceError):
    pass


class InvalidTransactionTypeError(FinanceError):
    pass


class TransactionNotFoundError(FinanceError):
    pass


class InvalidBudgetError(FinanceError):
    pass