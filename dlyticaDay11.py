# Name: Samir Khatiwada
# Assignment 3  Library Book Catalogue
# Date: 10 June 2026

# Task 1: Create Book class with instance attributes and class attribute
class Book:
    total_books = 0

    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

        # Increase total book count whenever a book is created
        Book.total_books += 1

    # Task 2: Create book object from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["genre"]
        )

    # Task 2: Return total number of books
    @classmethod
    def get_total(cls):
        return f"Total books registered: {cls.total_books}"

    # Task 3: Borrow a book
    def borrow(self):
        if not self.available:
            raise ValueError(f"'{self.title}' is already borrowed.")

        self.available = False

    # Task 3: Return a book
    def return_book(self):
        if self.available:
            raise ValueError(f"'{self.title}' is not currently borrowed.")

        self.available = True

    # Task 4: String representation of a book
    def __str__(self):
        status = "✓" if self.available else "✗"
        return f"[{status}] {self.title} | {self.author} | {self.genre}"


try:
    # Task 4: Create books
    b1 = Book("Python Crash Course", "Eric Matthes", "Programming")
    b2 = Book("Sapiens", "Yuval Noah Harari", "History")

    # Create book using from_dict()
    b3 = Book.from_dict({
        "title": "Deep Work",
        "author": "Cal Newport",
        "genre": "Productivity"
    })

    b4 = Book("Atomic Habits", "James Clear", "Self-Help")

    # Borrow two books
    b1.borrow()
    b2.borrow()



    print("=" * 40)
    print("Library Book Catalogue")
    print("=" * 40)
    
    # Print all books
    print(b1)
    print(b2)
    print(b3)
    print(b4)

    # Return one book
    b1.return_book()
    
    print("\nAfter returning a book:")
    print( "-" * 40)

    print(b1)

    # Test ValueError
    try:
        b2.borrow()
    except ValueError as e:
        print("\n" + "-" * 40)
        print(f"Error: {e}")
        print("\n" + "-" * 40)
        
    # Print total books
    print(f"{Book.get_total()}")

except ValueError as e:
    print(f"Error: {e}")