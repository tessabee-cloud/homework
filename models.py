from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, amount, category, date, comment=""):
        self.__id = transaction_id
        self.__amount = amount
        self.__category = category
        self.__date = date
        self.__comment = comment

    @property
    def id(self):
        return self.__id

    @property
    def amount(self):
        return self.__amount

    @property
    def category(self):
        return self.__category

    @property
    def date(self):
        return self.__date

    @property
    def comment(self):
        return self.__comment

    def to_dict(self):
        return {
            "id": self.__id,
            "amount": self.__amount,
            "category": self.__category,
            "date": self.__date,
            "comment": self.__comment
        }


class Income(Transaction):
    def __init__(self, transaction_id, amount, category, date, comment=""):
        super().__init__(
            transaction_id,
            amount,
            category,
            date,
            comment
        )

    @property
    def type(self):
        return "income"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.type
        return data


class Expense(Transaction):
    def __init__(self, transaction_id, amount, category, date, comment=""):
        super().__init__(
            transaction_id,
            amount,
            category,
            date,
            comment
        )

    @property
    def type(self):
        return "expense"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.type
        return data


class Budget:
    def __init__(self, category, limit):
        self.__category = category
        self.__limit = limit

    @property
    def category(self):
        return self.__category

    @property
    def limit(self):
        return self.__limit

    def to_dict(self):
        return {
            "category": self.__category,
            "limit": self.__limit
        }