import json
import random
import string
from pathlib import Path
from datetime import datetime


class Library:
    def __init__(self):
        path = Path(__file__).parent
        self.database = path / "library.json"
        self.data = self.load_data()

    def load_data(self):
        data = {"books": [], "members": []}

        if self.database.exists():
            with open(self.database, "r") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
        else:
            with open(self.database, "w") as f:
                json.dump(data, f, indent=4)

        return data

    def save_data(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4, default=str)

    @classmethod
    def create_id(cls, type):
        prefix = ""
        if type == "book":
            prefix += "B"
        else:
            prefix += "M"

        gen_id = ""
        for i in range(5):
            gen_id += random.choice(string.ascii_uppercase + string.digits)

        return prefix + "-" + gen_id

    def add_book(self):
        name = input("Name of the book: ")
        author = input("Author of the book: ")
        quantity = int(input("Quantity of the book: "))

        book = {
            "id": Library.create_id("book"),
            "title": name,
            "author": author,
            "total_copies": quantity,
            "available_copies": quantity,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.data["books"].append(book)
        self.save_data()

    def list_book(self):
        books = self.data["books"]

        if len(books) == 0:
            print("Sorry there are no books in Library")
        else:
            print(f"{"ID":10} {"Title":25} {"Author":25} {"Copies"}")
            for book in books:
                print(
                    f"{book["id"]:10} {book["title"][:20]:25} {book["author"][:20]:25} {book["total_copies"]}/{book["available_copies"]}"
                )

    def add_member(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")

        member = {
            "id": Library.create_id("member"),
            "name": name,
            "email": email,
            "borrowed": [],
        }

        self.data["members"].append(member)
        self.save_data()

    def list_member(self):
        members = self.data["members"]

        if not members:
            print("Sorry there are no members registered in Library")
        else:
            print(f"{"ID":10} {"Name":25} {"Email":25} {"Number of books borrowed"}")
            for member in members:
                print(
                    f"{member["id"]:10} {member["name"][:20]:25} {member["email"][:20]:25} {len(member["borrowed"])}"
                )

    def borrow_book(self):
        member_id = input("Enter the mermber ID : ").strip()
        members = [m for m in self.data["members"] if m["id"] == member_id]
        if not members:
            print("No such member exists")
            return

        member = members[0]

        book_id = input("Enter the book ID : ").strip()
        books = [b for b in self.data["books"] if b["id"] == book_id]

        if not books:
            print("Sorry there is no book for such ID")
            return

        book = books[0]

        if book["available_copies"] <= 0:
            print("Sorry there is no copy available")
        else:
            borrow_entry = {
                "book_id": book["id"],
                "title": book["title"],
                "borrow_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            member["borrowed"].append(borrow_entry)
            book["available_copies"] -= 1
            self.save_data()

    def return_book(self):
        member_id = input("Enter the mermber ID : ").strip()
        members = [m for m in self.data["members"] if m["id"] == member_id]
        if not members:
            print("No such member exists")
            return

        member = members[0]

        if not member["borrowed"]:
            print("This member didn't borrow any books")
            return

        print("Borrowed books: ")
        for i, b in enumerate(member["borrowed"], start=1):
            print(f"{i}. {b['title']} ({b['book_id']})")

        try:
            choice = int(input("enter number to return : - "))
            selected = member["borrowed"].pop(choice - 1)

            books = [bk for bk in self.data["books"] if bk["id"] == selected["book_id"]]
            if books:
                books[0]["available_copies"] += 1

            self.save_data()
        except Exception as err:
            print("Invalid Choice", err)


librarian = Library()

while True:
    print("=" * 50)
    print("Library Management System")
    print("=" * 50)
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Members")
    print("4. List members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit the portal")
    print("-" * 50)

    try:
        choice = int(input("Please Enter your choice: "))

        if choice == 1:
            librarian.add_book()

        elif choice == 2:
            librarian.list_book()

        elif choice == 3:
            librarian.add_member()

        elif choice == 4:
            librarian.list_member()

        elif choice == 5:
            librarian.borrow_book()

        elif choice == 6:
            librarian.return_book()
        else:
            exit(0)
    except Exception as err:
        print("Error occurred:", err)
