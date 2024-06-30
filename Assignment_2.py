                                           #ASSIGNMENT - 2
# You are tasked with creating a library management system. The system should allow users toperform the following operations:
class Library():
    def __init__(self):
        self.books = []
        self.book_set = set()
        self.categorized_books = {}
    def add_book(self, author, title, genre):
        return (author, title, genre)
    def add_to_library(self, book):
        if book not in self.book_set:
            self.books.append(book)
            self.book_set.add(book)
            self.categorize_books()
            print(f"Book '{book[1]}' by {book[0]} added to the library")
        else:
            print("Book already exists in the library")
    def remove_from_library(self, book):
        if book in self.book_set:
            self.books.remove(book)
            self.book_set.remove(book)
            self.categorize_books()
            print(f"Book '{book[1]}' removed from the library.")
        else:
            print(f"Book '{book[1]}' not found in the library.")
    def search_books(self, search):
        results = [book for book in self.books if search in book[0] or search in book[1]]
        if results:
            print("Search result:")
            for book in results:
                print(f"Title: {book[1]}, Author: {book[0]}, Genre: {book[2]}")
        else:
            print("No books matching the book you are searching.")
    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book[1]}, Author: {book[0]}, Genre: {book[2]}")
        else:
            print("The library is empty.")
    def categorize_books(self):
        self.categorized_books = {}
        for book in self.books:
            genre = book[2]
            if genre not in self.categorized_books:
                self.categorized_books[genre] = []
            self.categorized_books[genre].append(book)
        if self.categorized_books:
            for genre, books in self.categorized_books.items():
                print(f"Genre: {genre}")
                for book in books:
                    print(f"  Title: {book[1]}, Author: {book[0]}")
        else:
            print("The library is empty.")
lib = Library()
while True:
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. List all books")
    print("5. Categorize books")
    print("6. Exit")
    choice = input("Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):")
    if choice == 'Add':
        author = input("Enter author: ")
        title = input("Enter title: ")
        genre = input("Enter genre: ")
        book = lib.add_book(author, title, genre)
        lib.add_to_library(book)
    elif choice == 'Remove':
        author = input("Enter author of book to remove: ")
        book_to_remove = lib.add_book(author, title, genre)
        lib.remove_from_library(book_to_remove)
    elif choice == 'Search':
        search = input("Enter book name to search: ")
        lib.search_books(search)
    elif choice == 'List_book':
        lib.list_books()
    elif choice == 'Categorize':
        lib.categorize_books()
    elif choice == 'Exit':
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
# Output
# PS C:\Users\piyu\OneDrive\Desktop\python> & "C:/Program Files/Python312/python.exe" c:/Users/piyu/OneDrive/Desktop/python/Assignment2.py/123.py

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Add
# Enter author: Jane Austen
# Enter title: Pride and Prejudice
# Enter genre: Classic Romance
# Genre: Classic Romance
#   Title: Pride and Prejudice, Author: Jane Austen
# Book 'Pride and Prejudice' by Jane Austen added to the library

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Add
# Enter author: Aldous Huxley
# Enter title: Brave New World
# Enter genre: Science Fiction
# Genre: Classic Romance
#   Title: Pride and Prejudice, Author: Jane Austen
# Genre: Science Fiction
#   Title: Brave New World, Author: Aldous Huxley
# Book 'Brave New World' by Aldous Huxley added to the library

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Add
# Enter author: Gillian Flynn
# Enter title: Gone Girl
# Enter genre: Psychological Thriller
# Genre: Classic Romance
#   Title: Pride and Prejudice, Author: Jane Austen
# Genre: Science Fiction
#   Title: Brave New World, Author: Aldous Huxley
# Genre: Psychological Thriller
#   Title: Gone Girl, Author: Gillian Flynn
# Book 'Gone Girl' by Gillian Flynn added to the library

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):List_book
# Books in the library:
# Title: Pride and Prejudice, Author: Jane Austen, Genre: Classic Romance
# Title: Brave New World, Author: Aldous Huxley, Genre: Science Fiction
# Title: Gone Girl, Author: Gillian Flynn, Genre: Psychological Thriller

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Search
# Enter book name to search: Gone Girl
# Search result:
# Title: Gone Girl, Author: Gillian Flynn, Genre: Psychological Thriller

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Categorize
# Genre: Classic Romance
#   Title: Pride and Prejudice, Author: Jane Austen
# Genre: Science Fiction
#   Title: Brave New World, Author: Aldous Huxley
# Genre: Psychological Thriller
#   Title: Gone Girl, Author: Gillian Flynn

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Remove
# Enter author of book to remove: Gillian Flynn
# Genre: Classic Romance
#   Title: Pride and Prejudice, Author: Jane Austen
# Genre: Science Fiction
#   Title: Brave New World, Author: Aldous Huxley
# Book 'Gone Girl' removed from the library.

# Library Menu:
# 1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. List all books
# 5. Categorize books
# 6. Exit
# Enter your choice(Add/Remove/Search/List_book/Categorize/Exit):Exit
# Exiting the library system. Goodbye!