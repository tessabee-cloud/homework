import json
import os
from dataclasses import dataclass, asdict

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, ensure_ascii=False, indent=2)

def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    return []

def add_book(books):
    title = input("შეიყვანე სახელი: ")
    author = input("შეიყვანე ავტორი: ")
    while True:
        year_input = input("შეიყვანე წელი: ")
        if year_input.isdigit():
            year = int(year_input)
            break
        print("გთხოვთ შეიყვანოთ ციფრები!");
    new_id = max((b.id for b in books), default=0) + 1
    new_book = Book(id=new_id, title=title, author=author, year=year, available=True)
    books.append(new_book)
    print("✅ წიგნი დაემატა!")

def view_books(books):
    if not books:
        print("ბიბლიოთეკა ცარიელია.")
        return
    for b in books:
        status = "ხელმისაწვდომი" if b.available else "გაცემული"
        print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")

def search_books(books):
    search = input("შეიყვანე ძებნის სიტყვა: ").lower()
    found = [b for b in books if search in b.title.lower()]
    if not found:
        print("ჩანაწერი ვერ მოიძებნა.")
    else:
        for b in found:
            status = "ხელმისაწვდომი" if b.available else "გაცემული"
            print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")

def loan_book(books):
    id_input = input("შეიყვანე წიგნის ID გატანისთვის: ")
    if not id_input.isdigit():
        print("გთხოვთ შეიყვანოთ სწორი ID.")
        return
    book_id = int(id_input)
    for b in books:
        if b.id == book_id:
            if b.available:
                b.available = False
                print(f"✅ წიგნი '{b.title}' გატანილია.")
            else:
                print("წიგნი უკვე გაცემულია.")
            return
    print("წიგნი ID ვერ მოიძებნა.")

def return_book(books):
    id_input = input("შეიყვანე წიგნის ID დაბრუნებისთვის: ")
    if not id_input.isdigit():
        print("გთხოვთ შეიყვანოთ სწორი ID.")
        return
    book_id = int(id_input)
    for b in books:
        if b.id == book_id:
            b.available = True
            print(f"✅ წიგნი '{b.title}' დაბრუნებულია.")
            return
    print("წიგნი ID ვერ მოიძებნა.")

def statistics(books):
    total = len(books)
    available = sum(1 for b in books if b.available)
    loaned = total - available
    print(f"სულ წიგნები:   {total}")
    print(f"ხელმისაწვდომი:  {available}")
    print(f"გაცემული:       {loaned}")

def main():
    books = load_books()

    menu = """
1. წიგნის დამატება
2. ყველა წიგნის ნახვა
3. წიგნის ძებნა სახელით
4. წიგნის გატანა
5. წიგნის დაბრუნება
6. სტატისტიკა
7. მონაცემების შენახვა
8. გამოსვლა
"""

    while True:
        print(menu)
        choice = input("აირჩიე ოპცია: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            loan_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            statistics(books)
        elif choice == "7":
            save_books(books)
            print("✅ მონაცემები შენახულია.")
        elif choice == "8":
            save_books(books)
            print("მანქანა წარმატებით გაითიშა.")
            break
        else:
            print("შეიყვანე სწორი მეთოდი 1-8.")

if __name__ == "__main__":
    main()
