import sqlite3
#creat 4 functions for adding a book, update a book, delete a book and search for a book
def add_book(conn, cursor, title, author, qty):
    cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES (?,?,?)", (title, author, qty))
    conn.commit()
    print("Book added successfully.")

def update_book(conn, cursor, id, title, author, qty):
    cursor.execute("UPDATE books SET Title=?, Author=?, Qty=? WHERE id=?", (title, author, qty, id))
    conn.commit()
    print("Book updated successfully.")

def delete_book(conn, cursor, id):
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    print("Book deleted successfully.")

def search_book(cursor, title):
#if the user type lower case or the similar one, the book can still be searched

    cursor.execute("SELECT * FROM books WHERE LOWER(Title) LIKE ?", ('%' + title.lower() + '%',))
    book = cursor.fetchone()
    if book:
        print("ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Qty:", book[3])
    else:
        print("Book not found.")

def display_menu():
    print("\nMenu:")
    print("1. Add a new book")
    print("2. Update a book")
    print("3. Delete a book")
    print("4. Search for a book")
    print("0. Exit")

def main():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    if not cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'").fetchone():
        cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)")


        initial_books = [
            (3001, "A Tale of Two Cities", "Charles Dickens", 30),
            (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
            (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
            (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
            (3005, "Alice in Wonderland", "Lewis Carroll", 12)
        ]
        cursor.executemany("INSERT INTO books (id, Title, Author, Qty) VALUES (?,?,?,?)", initial_books)
        conn.commit()

    choice = -1
    while choice != '0':
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            qty = int(input("Enter book quantity: "))
            add_book(conn, cursor, title, author, qty)
        elif choice == '2':
            id = int(input("Enter the book id: "))
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            qty = int(input("Enter the book quantity: "))
            update_book(conn, cursor, id, title, author, qty)
        elif choice == '3':
            id = int(input("Enter the book id: "))
            delete_book(conn, cursor, id)
        elif choice == '4':
            title = input("Enter the book title: ")
            search_book(cursor, title)
        elif choice == '0':
            print("Exiting program.")
            conn.close()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
