class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' wasn't checked out.")


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        # Add a Book instance to the list of books
        self._books.append(book)

    def check_out_book(self, title):
        # Loop through books and find by title
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        # Loop through books and find by title to return
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def display_books(self):
        if not self._books:
            print("No books in the library.")
        else:
            for book in self._books:
                status = "Checked Out" if book._is_checked_out else "Available"
                print(f"Title: {book.title}, Author: {book.author}, Status: {status}")


# Example usage:
