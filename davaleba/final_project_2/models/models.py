from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, amount, category, date, comment="",user_id=None):
        self.__id = transaction_id
        self.__amount = amount
        self.__category = category
        self.__date = date
        self.__comment = comment
        self.__user_id = user_id

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

    @property
    def user_id(self):
        return self.__user_id

    def to_dict(self):
        return {
            "id": self.__id,
            "amount": self.__amount,
            "category": self.__category,
            "date": self.__date,
            "comment": self.__comment,
            "user_id": self.__user_id
        }


class Income(Transaction):
    def __init__(self, transaction_id, amount, category, date, comment="",user_id=None):
        super().__init__(
            transaction_id,
            amount,
            category,
            date,
            comment,
            user_id
        )

    @property
    def type(self):
        return "income"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.type
        return data


class Expense(Transaction):
    def __init__(self, transaction_id, amount, category, date, comment="",user_id=None):
        super().__init__(
            transaction_id,
            amount,
            category,
            date,
            comment,
            user_id
        )

    @property
    def type(self):
        return "expense"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.type
        return data


class Budget:
    def __init__(self, category, limit,user_id=None):
        self.__category = category
        self.__limit = limit
        self.__user_id = user_id

    @property
    def category(self):
        return self.__category

    @property
    def limit(self):
        return self.__limit
    @property
    def user_id(self):
        return self.__user_id

    def to_dict(self):
        return {
            "category": self.__category,
            "limit": self.__limit,
            "user_id": self.__user_id
        }