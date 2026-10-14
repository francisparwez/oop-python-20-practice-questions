# 15. Library Management System 📚
# Create:
#     Book
#     Library
# Book should contain:
#     title
#     author
#     isbn
#     available
# Library should have methods:
#     add_book()
#     remove_book()
#     borrow_book()
#     return_book()
#     display_books()

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                print(f"Successfully removed '{b.title}' from the library.")
                return
                
        print(f"Cannot remove book: ISBN {isbn} does not exist.")

        
    def display_books(self):
        if not self.books:
            print('Library Is Empty')
            return
        
        print("\n--- Library Books ---")
        for b in self.books:
            print(f'Title: {b.title}')
            print(f'Author: {b.author}')
            print(f'ISBN: {b.isbn}')
            print(f'Available: {b.available}')
            print("---------------------\n")
            
    def borrow_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.available:
                    b.available = False
                    print(f"Successfully borrowed '{b.title}'!")
                else:
                    print(f"Sorry, '{b.title}' is already borrowed.")
                return
        
        print(f"Book with ISBN {isbn} does not exist in the library.")
        
    
    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if not b.available:
                    b.available = True
                    print(f"Successfully returned '{b.title}'!")
                else:
                    print(f"'{b.title}' is already available in the library.")
                return 
        print(f"Book with ISBN {isbn} does not exist.")

        
if __name__ == '__main__':
    book1 = Book("Harry Potter", "J.K. Rowling", "12345")
    book2 = Book("The Hobbit", "J.R.R. Tolkien", "67890")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "11223")
    book4 = Book("1984", "George Orwell", "44556")
    book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", "77889")
    book6 = Book("Pride and Prejudice", "Jane Austen", "99001")

    
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    
    library.display_books()
    
    library.borrow_book("12345")
    library.borrow_book("11223")
    library.return_book("12345")
    
    library.remove_book("67890")
    library.display_books() 