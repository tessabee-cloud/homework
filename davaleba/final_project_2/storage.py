import json
import csv

from models.models import Income, Expense, Budget


class Storage:
    def __init__(self, json_file="data.json", csv_file="transactions.csv"):
        self.json_file = json_file
        self.csv_file = csv_file

    def save_data(self, transactions, budgets):
        data = {
            "transactions": [
                transaction.to_dict()
                for transaction in transactions
            ],
            "budgets": [
                budget.to_dict()
                for budget in budgets.values()
            ]
        }

        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_data(self):
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return [], {}
        except json.JSONDecodeError:
            print("Warning: data.json is corrupted.")
            return [], {}

        transactions = []

        for item in data.get("transactions", []):
            if item["type"] == "income":
                transaction = Income(
                    item["id"],
                    item["amount"],
                    item["category"],
                    item["date"],
                    item["comment"],
                    item.get("user_id")
                )
            else:
                transaction = Expense(
                    item["id"],
                    item["amount"],
                    item["category"],
                    item["date"],
                    item["comment"],
                    item.get("user_id")
                )

            transactions.append(transaction)

        budgets = {}

        for item in data.get("budgets", []):
            budget = Budget(
                item["category"],
                item["limit"],
                item.get("user_id")
            )

            budgets[item["category"]] = budget

        return transactions, budgets

    def export_csv(self, transactions):
        with open(
            self.csv_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "id",
                "type",
                "amount",
                "category",
                "date",
                "comment",
                "user_id"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for transaction in transactions:
                writer.writerow(transaction.to_dict())