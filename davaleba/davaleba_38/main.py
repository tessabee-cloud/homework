from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import select
from models import engine, Customer, Order, Product, OrderItem, Base

Base.metadata.create_all(engine)




Session = sessionmaker(bind=engine)
session = Session()




customers = [
    Customer(name="John", email="john@gmail.com"),
    Customer(name="Anna", email="anna@gmail.com"),
    Customer(name="Kate", email="kate@gmail.com"),
    Customer(name="Bob", email="bob@gmail.com"),
    Customer(name="Patrick", email="patrick@gmail.com")
]

session.add_all(customers)
session.commit()




products = [
    Product(name="Laptop", price=1000),
    Product(name="Phone", price=700),
    Product(name="Keyboard", price=80),
    Product(name="Mouse", price=40),
    Product(name="Monitor", price=300),
    Product(name="Headphones", price=120),
    Product(name="Tablet", price=500),
    Product(name="Camera", price=900)
]

session.add_all(products)
session.commit()




john = session.query(Customer).filter_by(name="John").first()
anna = session.query(Customer).filter_by(name="Anna").first()
kate = session.query(Customer).filter_by(name="Kate").first()
bob = session.query(Customer).filter_by(name="Bob").first()
patrick = session.query(Customer).filter_by(name="Patrick").first()

order1 = Order(customer=john)
order2 = Order(customer=john)
order3 = Order(customer=anna)
order4 = Order(customer=kate)
order5 = Order(customer=bob)

session.add_all([
    order1,
    order2,
    order3,
    order4,
    order5
])

session.commit()




laptop = session.query(Product).filter_by(name="Laptop").first()
phone = session.query(Product).filter_by(name="Phone").first()
keyboard = session.query(Product).filter_by(name="Keyboard").first()
mouse = session.query(Product).filter_by(name="Mouse").first()
monitor = session.query(Product).filter_by(name="Monitor").first()
headphones = session.query(Product).filter_by(name="Headphones").first()
tablet = session.query(Product).filter_by(name="Tablet").first()
camera = session.query(Product).filter_by(name="Camera").first()




order1.items = [
    OrderItem(product=laptop, quantity=1),
    OrderItem(product=mouse, quantity=2)
]

order2.items = [
    OrderItem(product=phone, quantity=1),
    OrderItem(product=headphones, quantity=1)
]

order3.items = [
    OrderItem(product=keyboard, quantity=1),
    OrderItem(product=monitor, quantity=1)
]

order4.items = [
    OrderItem(product=tablet, quantity=2)
]

order5.items = [
    OrderItem(product=camera, quantity=1),
    OrderItem(product=mouse, quantity=1)
]

session.commit()




print("\n========== ALL CUSTOMERS ==========")

all_customers = session.query(Customer).all()

for customer in all_customers:
    print(f"ID: {customer.id}")
    print(f"Name: {customer.name}")
    print(f"Email: {customer.email}")
    print()




print("\n========== JOHN'S ORDERS ==========")

john = (
    session.query(Customer)
    .options(joinedload(Customer.orders))
    .filter(Customer.name == "John")
    .first()
)

if john:
    print(f"Customer: {john.name}")

    for order in john.orders:
        print(f"Order ID: {order.id}")
        print(f"Order Date: {order.order_date}")
        print()




print("\n========== ORDER 1 PRODUCTS ==========")

order = (
    session.query(Order)
    .options(
        joinedload(Order.items)
        .joinedload(OrderItem.product)
    )
    .filter(Order.id == order1.id)
    .first()
)

if order:
    print(f"Order ID: {order.id}")

    for item in order.items:
        print(f"Product: {item.product.name}")
        print(f"Quantity: {item.quantity}")
        print()




print("\n========== NEW ORDER ==========")

customer = (
    session.query(Customer)
    .filter(Customer.name == "Patrick")
    .first()
)

new_order = Order(
    customer=customer
)

new_order.items = [
    OrderItem(product=laptop, quantity=1),
    OrderItem(product=keyboard, quantity=1),
    OrderItem(product=headphones, quantity=2)
]

session.add(new_order)
session.commit()

print(f"New order created: {new_order.id}")




print("\n========== UPDATE PRODUCT ==========")

laptop = (
    session.query(Product)
    .filter(Product.name == "Laptop")
    .first()
)

if laptop:
    print(f"Old price: {laptop.price}")

    laptop.price = 1200

    session.commit()

    print(f"New price: {laptop.price}")




session.close()

print("\nSession closed.")