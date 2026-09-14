from main import (
    add_transaction,
    view_transactions,
    filter_transactions,
    delete_transaction,
    set_budget,
    monthly_summary,
    general_summary,
    export_csv
)


while True:
    print('\n--- PERSONAL FINANCE TRACKER ---')
    print('1. Add transaction')
    print('2. View transactions')
    print('3. Filter transactions')
    print('4. Delete transaction')
    print('5. Set category budget')
    print('6. Monthly summary')
    print('7. General summary')
    print('8. Export transactions to CSV')
    print('9. EXIT')

    choice = input('Choose: ')

    try:
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()

        elif choice == '3':
            filter_transactions()

        elif choice == '4':
            delete_transaction()

        elif choice == '5':
            set_budget(category=input('Enter category: '),limit=float(input('Enter budget limit: ')))

        elif choice == '6':
            monthly_summary()

        elif choice == '7':
            general_summary()

        elif choice == '8':
            export_csv()

        elif choice == '9':
            print('Exiting the application...')
            break

        else:
            print('invalid choice')

    except Exception as e:
        print(f'Error: {e}')