class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.librarians = []
        self.patrons = []

    def borrowBook(self, book):
        if book in self.books and not book.borrowed:
            book.borrowed = True
            print(book.title + " has been borrowed")
        else:
            print(book.title + " is not available")

    def returnBook(self, book):
        if book not in self.books:
            self.books.append(book)
        book.borrowed = False
        print(book.title + " has been returned")

    def addLibrarian(self, librarian):
        self.librarians.append(librarian)
        print(librarian.name + " has been added")

    def removeLibrarian(self, librarian):
        self.librarians.remove(librarian)
        print(librarian.name + " has been removed")

    def addBook(self, book):
        self.books.append(book)
        print(book.title, 'was added')

    def removeBook(self, book):
        self.books.remove(book)
        print(book.title, 'was removed')

    def addPatron(self, patron):
        self.patrons.append(patron)
        print(patron.name + " was added")

    def removePatron(self, patron):
        self.patrons.remove(patron)
        print(patron.name + " was removed")

    def listBooks(self):
        return (str(book) for book in self.books)

    def listPatrons(self):
        return (str(patron) for patron in self.patrons)

    def listLibrarians(self):
        return (str(librarian) for librarian in self.librarians)
