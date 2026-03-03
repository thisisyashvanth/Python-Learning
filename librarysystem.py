class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Description: {self.description}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")
    
    def view_books(self):
        if not self.books:
            print("Sorry, no books currently available")
        else:
            for book in self.books:
                print(book)
    
    def search_book(self, title):
        


library = Library()

while True:
    print()
    print("Welcome to Library Management Application")
    print("-----------------------------------------")
    print("Press 1 for Adding Books")
    print("Press 2 for Viewing Books")
    print("Press 3 for Searching Books")
    print("Press 4 to Exit")
    print()
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter title: ")
        author = input("Enter author: ")
        description = input("Enter description: ")
        book = Book(title, author, description)
        library.add_book(book)

    elif choice == 2:
        library.view_books()
    
    elif choice == 3:
        

    elif choice == 4:
        print("Thank You")
        break