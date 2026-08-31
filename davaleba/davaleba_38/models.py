from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)



engine = create_engine("postgresql://postgres:1810@localhost:5432/pp-38")




class Base(DeclarativeBase):
    pass




class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True
    )

    # One Customer -> Many Orders
    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer"
    )

    def __repr__(self):
        return (
            f"Customer(id={self.id}, "
            f"name='{self.name}', "
            f"email='{self.email}')"
        )




class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id")
    )

    order_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    # Many Orders -> One Customer
    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )

    # One Order -> Many OrderItems
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order"
    )

    def __repr__(self):
        return (
            f"Order(id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"order_date={self.order_date})"
        )




class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    price: Mapped[int] = mapped_column(
        Integer
    )

    # One Product -> Many OrderItems
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )

    def __repr__(self):
        return (
            f"Product(id={self.id}, "
            f"name='{self.name}', "
            f"price={self.price})"
        )




class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id")
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )

    # Many OrderItems -> One Order
    order: Mapped["Order"] = relationship(
        back_populates="items"
    )

    # Many OrderItems -> One Product
    product: Mapped["Product"] = relationship(
        back_populates="order_items"
    )

    def __repr__(self):
        return (
            f"OrderItem(id={self.id}, "
            f"order_id={self.order_id}, "
            f"product_id={self.product_id}, "
            f"quantity={self.quantity})"
        )