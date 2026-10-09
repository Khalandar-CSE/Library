class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.__total = copies    # how many the library owns
        self.__copies = copies   # how many are on the shelf now

    def __str__(self):
        return f"{self.title} by {self.author}"

    def add_copies(self, n=1):
        self.__total += n
        self.__copies += n

    def available(self):
        return self.__copies

    def borrow(self):
        if self.__copies == 0:
            return False
        self.__copies -= 1
        return True

    def give_back(self):
        if self.__copies >= self.__total:   # nothing was out on loan
            return False
        self.__copies += 1
        return True


class Library:
    def __init__(self):
        self.books = []

    def find(self, title):
        for book in self.books:          # compare titles, not objects
            if book.title == title:
                return book
        return None

    def add_book(self, title, author, copies=1):
        book = self.find(title)
        if book:
            book.add_copies(copies)      # same title: raise the count
        else:
            self.books.append(Book(title, author, copies))

    def show_books(self):
        for book in self.books:
            print(f"{book} - {book.available()} available")

    def borrow_book(self, title):
        book = self.find(title)
        if book is None:
            print("We don't have that book.")
        elif book.borrow():
            print(f"You borrowed {book.title}.")
        else:
            print(f"Sorry, no copies of {book.title} left.")

    def return_book(self, title):
        book = self.find(title)
        if book is None:
            print("We don't have that book.")
        elif book.give_back():
            print(f"Thanks for returning {book.title}.")
        else:
            print(f"Nothing of {book.title} was out on loan.")


if __name__ == "__main__":
    lib = Library()
    lib.add_book("Ikigai", "Hector Garcia", 1)
    lib.add_book("Ikigai", "Hector Garcia", 1)   # becomes 2 copies, one entry
    lib.show_books()
    lib.borrow_book("Ikigai")
    lib.borrow_book("Ikigai")
    lib.borrow_book("Ikigai")                    # refused, count stays 0
    lib.return_book("Ikigai")
    lib.show_books()