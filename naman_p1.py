class Book:
    def __init__(self, book_id, title, author):
        
        self.book_id = book_id
        self.title = title
        self.author = author  
        self.is_borrowed = False
    
    def display(self):
        status="borrowed" if self.is_borrowed else "avalaible"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")
        
        
class Patron:
    def __init__(self, patron_id, name):
        
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []
    
    
def display(self):   
    print(f"Patron ID: {self.patron_id}, Name: {self.name}")
    print("Borrowed Books:", self.borrowed_books)
    
class Library:
    def __init__(self, book_name, author, available=True):       
        self.books_name = {}
        self.author = {}
    
    def check_out(self):
        
        if self.available:
            self.avalaible = False            
            print(f"'{self.book_name}' by {self.author} has been checked out.")
        else:           
            print(f"'{self.book_name}' by {self.author} is currently unavailable.")
        
        
    def add_book(self, book):
        self.book[book.book_id]=book
        print(f"book'{book.title}' added successfully.")
        
        
    def register_patron(self, patron):
        
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")
# Borrow a book

def borrow_book(self, patron_id, book_id):
    if patron_id not in self.patrons:        
        print("Patron not found.")
        
        return
    if book_id not in self.books:        
        print("Book not found.")
        return
    book = self.books[book_id]
    patron = self.patrons[patron_id]
    if book.is_borrowed:
        print(f"Book'{book.title}' is already borrowed.")
    else:
        book.is_borrowed = True
        patron.borrowed_books.append(book.title)
        print(f"{patron.name} borrowed'{book.title}'.")