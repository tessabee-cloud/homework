import pandas as pd
from datetime import datetime

PRODUCTS_FILE = "products.csv"
LOG_FILE = "log.txt"


def log_action(user, action, info=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(
            f"[{timestamp}] USER={user} | ACTION={action} {info}\n"
        )


def show_all_products(user):
    df = pd.read_csv(PRODUCTS_FILE)

    print(df)

    log_action(user, "VIEW_ALL_PRODUCTS")


def get_product_by_id(user):
    product_id = int(input("Enter product id: "))

    df = pd.read_csv(PRODUCTS_FILE)

    product = df[df["id"] == product_id]

    if product.empty:
        print("Product not found.")
    else:
        print(product)

        log_action(
            user,
            "GET_PRODUCT",
            f"| PRODUCT_ID={product_id}"
        )


def add_product(user):
    df = pd.read_csv(PRODUCTS_FILE)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    if df.empty:
        new_id = 1
    else:
        new_id = df["id"].max() + 1

    new_product = pd.DataFrame({
        "id": [new_id],
        "name": [name],
        "price": [price],
        "stock": [stock]
    })

    df = pd.concat([df, new_product], ignore_index=True)

    df.to_csv(PRODUCTS_FILE, index=False)

    print("Product added successfully.")

    log_action(
        user,
        "ADD_PRODUCT",
        f"| NAME={name}"
    )


def delete_product(user):
    product_id = int(input("Enter product id to delete: "))

    df = pd.read_csv(PRODUCTS_FILE)

    if product_id not in df["id"].values:
        print("Product not found.")
        return

    df = df[df["id"] != product_id]

    df.to_csv(PRODUCTS_FILE, index=False)

    print("Product deleted successfully.")

    log_action(
        user,
        "DELETE_PRODUCT",
        f"| PRODUCT_ID={product_id}"
    )


def main():
    user = input("Enter your name: ")

    while True:
        print("\n----- MENU -----")
        print("1. Show all products")
        print("2. Get product by ID")
        print("3. Add product")
        print("4. Delete product")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all_products(user)

        elif choice == "2":
            get_product_by_id(user)

        elif choice == "3":
            add_product(user)

        elif choice == "4":
            delete_product(user)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()