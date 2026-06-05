
import csv
from datetime import datetime

from davaleba.davaleba_11 import fieldnames

product_file= "products.csv"
log_file= "log.txt"


def log_action(user, action, info=""):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(log_file, 'a', newline='') as file:
        file.write(f"{current_time}\t{user}\t{action}\t{info}\n")

def read_products():
    products = []

    with open(product_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append(row)

    return products

def write_products(products):
    with open(product_file, "w", newline="") as file:
        fieldnames= ['id', 'name', 'price', 'stock']

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def show_all_products(user):
    products = read_products()

    for product in products:
        print(product)

    log_action(user, 'VIEW_ALL_PRODUCTS')

def get_product_by_id(user):
    product_id = input("Enter product id: ")

    products = read_products()

    for product in products:
        if product['id'] == product_id:
            print(product)
            log_action(
                user,
                'GET_PRODUCT',
                f' /PRODUCT_ID = {product_id}\n'
            )
            return
        else:
            print('product not found')

def add_product(user):
    products = read_products()

    name = input("Enter product name: ")
    price = input("Enter product price: ")
    stock = input("Enter product quantity: ")

    if products:
        new_id = str(max(int(product['id']) for product in products) + 1)
    else:
        new_id= '1'

    products.append(
        {
            'id': new_id,
            'name': name,
            'price': price,
            'stock': stock
        }
    )

    write_products(products)

    log_action(
        user,
        'ADD_PRODUCT',
        f' / NAME = {name}\n'
    )

    print('Product added successfully.')

def delete_product(user):
    product_id = input("Enter product id to delete: ")

    products = read_products()

    for product in products:
        if product['id'] == product_id:
            products.remove(product)

            write_products(products)

            log_action(
                user,
                'DELETE_PRODUCT',
                f' /PRODUCT_ID = {product_id}\n'
            )

            print('Product deleted successfully.')
            return
        else:
            print('product not found')

def main():
    user = input("Enter your name: ")

    while True:
        print('/n---MENU---')
        print('1. show all products')
        print('2. get product by id')
        print('3. add product')
        print('4. delete product')
        print('5. exit')

        choice = input('choose an option: ')
        if choice == '1':
            show_all_products(user)

        elif choice == '2':
            get_product_by_id(user)

        elif choice == '3':
            add_product(user)

        elif choice == '4':
            delete_product(user)

        elif choice == '5':
            print('goodbye!')
            break

        else:
            print('invalid choice')


main()


