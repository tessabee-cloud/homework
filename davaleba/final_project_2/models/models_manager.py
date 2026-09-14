from datetime import datetime


from models.models import Income, Expense, Budget
from decorators import validate_amount

from exceptions import (
    InvalidDateError,
    InvalidTransactionTypeError,
    TransactionNotFoundError,
    InvalidBudgetError
)



class FinanceManager:

    def __init__(self, storage):
        self.storage = storage
        self.transactions = []
        self.budgets = {}
        # self.budgets_notifications = {}

        self.load_data()

    # def check_budget_notifications(self):
    #     notifications = []
    #
    #     for category, budgets in self.budgets.items():
    #
    #         spent = sum(
    #             transaction.amount
    #             for transaction in self.transactions
    #             if transaction.type == 'expense'
    #             and transaction.category.lower() == category.lower()
    #         )
    #
    #         percentage = (spent / budgets.limit) * 100 if budgets.limit > 0 else 0
    #
    #         if percentage >= 100:
    #             current_level = 100
    #         elif percentage >= 90:
    #             current_level = 90
    #         elif percentage >= 70:
    #             current_level = 70
    #         elif percentage >= 50:
    #             current_level = 50
    #         else:
    #             current_level = 0
    #
    #         previous_level = self.budgets_notifications.get(category, 0)
    #
    #         if current_level > previous_level:
    #
    #             if current_level >= 100:
    #                 notifications.append(
    #                     f'🚨{category}:you have exceeded your budget!'
    #                 )
    #             elif  current_level >= 90:
    #                 notifications.append(
    #                     f'🔴{category}:you have used 90% of your budget!'
    #                 )
    #             elif current_level >= 70:
    #                 notifications.append(
    #                     f'🟠{category}:you have used 70% of your budget!'
    #                 )
    #             elif current_level >= 50:
    #                 notifications.append(
    #                     f'🟡{category}:you have used 50% of your budget!
    #                 )
    #
    #             self.budgets_notifications[category] = current_level
    #
    #         return notifications

    def load_data(self):
        self.transactions, self.budgets = self.storage.load_data()

    def save_data(self):
        self.storage.save_data(
            self.transactions,
            self.budgets
        )

    def get_next_id(self):
        if not self.transactions:
            return 1

        return max(
            transaction.id
            for transaction in self.transactions
        ) + 1

    @validate_amount('amount')
    def add_transaction(
        self,
        amount,
        transaction_type,
        category,
        date,
        comment="",
        user_id=None
    ):

        transaction_type = transaction_type.lower()

        transaction_id = self.get_next_id()

        if transaction_type == "income":
            transaction = Income(
                transaction_id,
                amount,
                category,
                date,
                comment,
                user_id
            )
        else:
            transaction = Expense(
                transaction_id,
                amount,
                category,
                date,
                comment,
                user_id
            )

        if transaction_type not in ["income", "expense"]:
            raise InvalidTransactionTypeError(
                "Transaction type must be 'income' or 'expense'."
            )

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise InvalidDateError(
                "Date must have format YYYY-MM-DD."
            )

        transaction_id = self.get_next_id()

        if transaction_type == "income":
            transaction = Income(
                transaction_id,
                amount,
                category,
                date,
                comment,
                user_id
            )
        else:
            transaction = Expense(
                transaction_id,
                amount,
                category,
                date,
                comment,
                user_id
            )

        self.transactions.append(transaction)
        self.save_data()

    def get_transactions(self):
        return self.transactions

    def filter_by_category(self, category):
        return [
            transaction
            for transaction in self.transactions
            if transaction.category.lower() == category.lower()
        ]

    def filter_by_date(self, date):
        return [
            transaction
            for transaction in self.transactions
            if transaction.date == date
        ]

    def filter_by_date_range(self, start_date, end_date):
        try:
            start = datetime.strptime(
                start_date,
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                end_date,
                "%Y-%m-%d"
            )
        except ValueError:
            raise InvalidDateError(
                "Dates must have format YYYY-MM-DD."
            )

        return [
            transaction
            for transaction in self.transactions
            if start <= datetime.strptime(
                transaction.date,
                "%Y-%m-%d"
            ) <= end
        ]

    def delete_transaction(self, transaction_id):
        try:
            transaction_id = int(transaction_id)
        except ValueError:
            raise TransactionNotFoundError(
                "Transaction ID must be a number."
            )

        for transaction in self.transactions:
            if transaction.id == transaction_id:
                self.transactions.remove(transaction)
                self.save_data()
                return

        raise TransactionNotFoundError(
            "Transaction not found."
        )





    @validate_amount('limit')
    def set_budget(self, category, limit,user_id=None):
        category = category.strip()

        if not category:
            raise InvalidBudgetError(
                "Category cannot be empty."
            )

        budget = Budget(
            category,
            limit,
            user_id
        )

        self.budgets[category] = budget
        self.save_data()


    def calculate_summary(self, transactions=None):
        if transactions is None:
            transactions = self.transactions

        income = sum(
            transaction.amount
            for transaction in transactions
            if isinstance(transaction, Income)
        )

        expenses = sum(
            transaction.amount
            for transaction in transactions
            if isinstance(transaction, Expense)
        )

        balance = income - expenses

        return income, expenses, balance

    def monthly_summary(self, year, month):
        try:
            year = int(year)
            month = int(month)

            if month < 1 or month > 12:
                raise ValueError

        except ValueError:
            raise InvalidDateError(
                "Year or month is invalid."
            )

        transactions = [
            transaction
            for transaction in self.transactions
            if datetime.strptime(
                transaction.date,
                "%Y-%m-%d"
            ).year == year
            and datetime.strptime(
                transaction.date,
                "%Y-%m-%d"
            ).month == month
        ]

        income, expenses, balance = self.calculate_summary(
            transactions
        )

        return transactions, income, expenses, balance

    def get_budget_status(self, transactions=None,user_id=None):
        if transactions is None:
            transactions = self.transactions

        expenses_by_category = {}

        for transaction in transactions:
            if isinstance(transaction, Expense):
                category = transaction.category

                expenses_by_category[category] = (
                    expenses_by_category.get(category, 0)
                    + transaction.amount
                )

        status = []

        for category, budget in self.budgets.items():
            if user_id is not None and budget.user_id != user_id:
                continue
            spent = expenses_by_category.get(
                category,
                0
            )

            remaining = budget.limit - spent

            status.append({
                "category": category,
                "limit": budget.limit,
                "spent": spent,
                "remaining": remaining,
                "over_limit": spent > budget.limit
            })

        return status