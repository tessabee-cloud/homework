from storage import Storage
from models.models_manager import FinanceManager

storage = Storage()
manager = FinanceManager(storage)


def add_transaction():
    transaction_type = input(
        'Type (income/expense): '
    ).strip()

    amount = input('Amount: ').strip()
    category = input('Category: ').strip()
    date = input('Date (YYYY-MM-DD): ').strip()
    comment = input('Comment: ').strip()

    manager.add_transaction(
        amount,
        transaction_type,
        category,
        date,
        comment
    )

    print('Transaction added successfully!')


def view_transactions():
    transactions = manager.get_transactions()

    if not transactions:
        print('No transactions found.')
        return

    print('\n--- TRANSACTIONS ---')

    for transaction in transactions:
        print(
            f'ID: {transaction.id} | '
            f'Type: {transaction.type} | '
            f'Amount: {transaction.amount:.2f} ₾ | '
            f'Category: {transaction.category} | '
            f'Date: {transaction.date} | '
            f'Comment: {transaction.comment}'
        )


def filter_transactions():
    print('\n--- FILTER TRANSACTIONS ---')
    print('1. By category')
    print('2. By exact date')
    print('3. By date range')

    choice = input('Choose: ').strip()

    if choice == '1':
        category = input('Category: ').strip()

        transactions = manager.filter_by_category(
            category
        )

    elif choice == '2':
        date = input(
            'Date (YYYY-MM-DD): '
        ).strip()

        transactions = manager.filter_by_date(
            date
        )

    elif choice == '3':
        start_date = input(
            'Start date (YYYY-MM-DD): '
        ).strip()

        end_date = input(
            'End date (YYYY-MM-DD): '
        ).strip()

        transactions = manager.filter_by_date_range(
            start_date,
            end_date
        )

    else:
        print('Invalid choice')
        return

    if not transactions:
        print('No transactions found.')
        return

    for transaction in transactions:
        print(
            f'ID: {transaction.id} | '
            f'{transaction.type} | '
            f'{transaction.amount:.2f} ₾ | '
            f'{transaction.category} | '
            f'{transaction.date} | '
            f'{transaction.comment}'
        )


def delete_transaction():
    transaction_id = input(
        'Enter transaction ID: '
    ).strip()

    manager.delete_transaction(transaction_id)

    print('Transaction deleted successfully!')


def set_budget(category,limit):

    category = category
    limit = limit

    manager.set_budget(
        category,
        limit
    )

    print('Budget limit saved successfully!')


def monthly_summary():
    year = input('Year: ').strip()
    month = input('Month: ').strip()

    (
        transactions,
        income,
        expenses,
        balance
    ) = manager.monthly_summary(
        year,
        month
    )

    print('\n--- MONTHLY SUMMARY ---')
    print(f'Income: {income:.2f} ₾')
    print(f'Expenses: {expenses:.2f} ₾')
    print(f'Balance: {balance:.2f} ₾')

    print('\n--- BUDGET STATUS ---')

    statuses = manager.get_budget_status(
        transactions
    )

    if not statuses:
        print('No budgets configured.')
        return

    for status in statuses:
        if status['over_limit']:
            message = 'OVER LIMIT!'
        else:
            message = 'OK'

        print(
            f"{status['category']}: "
            f"{status['spent']:.2f} / "
            f"{status['limit']:.2f} ₾ - "
            f"{message}"
        )


def general_summary():
    income, expenses, balance = (
        manager.calculate_summary()
    )

    print('\n--- GENERAL SUMMARY ---')
    print(f'Total income: {income:.2f} ₾')
    print(f'Total expenses: {expenses:.2f} ₾')
    print(f'Balance: {balance:.2f} ₾')

    print('\n--- BUDGET STATUS ---')

    statuses = manager.get_budget_status()

    if not statuses:
        print('No budgets configured.')
        return

    for status in statuses:
        if status['over_limit']:
            message = 'OVER LIMIT!'
        else:
            message = 'OK'

        print(
            f"{status['category']}: "
            f"{status['spent']:.2f} / "
            f"{status['limit']:.2f} ₾ - "
            f"{message}"
        )


def export_csv():
    manager.storage.export_csv(
        manager.transactions
    )

    print(
        'Transactions exported to transactions.csv!'
    )



#notifications
#
# notifications = manager.check_budget_notifications()
#
# for notification in notifications:
#     print(notification)