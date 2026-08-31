from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker



engine = create_engine("postgresql://postgres:1810@localhost:5432/pp-38")



class Base(DeclarativeBase):
    pass



class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))
    publish_year: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return (f"Book id={self.id}, "
                f"title='{self.title}', "
                f"author='{self.author}', "
                f"publish_year={self.publish_year}")



Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)
session = Session()



books = [
    Book(title="Atomic Habits", author="James Clear", publish_year=2018),
    Book(title="The Silent Patient", author="Alex Michaelides", publish_year=2019),
    Book(title="The Hobbit", author="J.R.R. Tolkien", publish_year=1937),
    Book(title="The Midnight Library", author="Matt Haig", publish_year=2020),
    Book(title="Clean Code", author="Robert C. Martin", publish_year=2008)
]

session.add_all(books)
session.commit()




print("\nყველა წიგნი:")
all_books = session.query(Book).all()
for book in all_books:
    print(book)


print("\nწიგნი ID = 1:")
book = session.query(Book).filter(Book.id == 1).first()
print(book)


print("\n2015 წლის შემდეგ გამოცემული წიგნები:")
new_books = session.query(Book).filter(Book.publish_year > 2015).all()
for book in new_books:
    print(book)



book = session.query(Book).filter(Book.id == 2).first()

if book:
    book.author = "Updated Author"
    session.commit()
    print("\nავტორი წარმატებით განახლდა.")



book = session.query(Book).filter(Book.id == 5).first()

if book:
    session.delete(book)
    session.commit()
    print("წიგნი წარმატებით წაიშალა.")



session.close()