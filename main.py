import time

from Library import Library
from Books import Books
from People import Librarian, Patron

TheLibrary = Library('Fuzuli', 'Wolska 31, Warszawa')
print(TheLibrary.name + " is located in " + TheLibrary.address)
print()

while True:
    Userwant = input("What would you like to do (Add Book, Remove Book, Add Librarian, Remove Librarian, Add Patron, "
                     "Remove Patron, Borrow Book, Return Book, List Books, List Patrons, List Librarians or END): ")\
        .strip().upper()

    if Userwant == "ADD BOOK":
        title = input("Please enter the title: ")
        pages = input("Please enter the number of pages: ")
        genre = input("Please enter the genre: ")
        author = input("Please enter the author: ")
        isbn = input("Please enter the ISBN code: ")
        borrowed = False
        newBook = Books(title, pages, genre, author, isbn, borrowed)
        TheLibrary.addBook(newBook)

    elif Userwant == "REMOVE BOOK":
        title = input("Please enter the title: ")
        book = next((b for b in TheLibrary.books if b.title == title), None)
        if book:
            TheLibrary.removeBook(book)
        else:
            print("Book not found.")

    elif Userwant == "ADD LIBRARIAN":
        name = input("Please enter librarian name: ")
        librarian_id = input("Please assign an ID: ")
        newLibrarian = Librarian(name, librarian_id)
        TheLibrary.addLibrarian(newLibrarian)

    elif Userwant == "REMOVE LIBRARIAN":
        name = input("Please enter librarian name: ")
        librarian = next((l for l in TheLibrary.librarians if l.name == name), None)
        if librarian:
            TheLibrary.removeLibrarian(librarian)
        else:
            print("Librarian not found.")

    elif Userwant == "ADD PATRON":
        name = input("Please enter patron name: ")
        patron_id = input("Please assign an ID: ")
        newPatron = Patron(name, patron_id)
        TheLibrary.addPatron(newPatron)

    elif Userwant == "REMOVE PATRON":
        name = input("Please enter patron name: ")
        patron = next((p for p in TheLibrary.patrons if p.name == name), None)
        if patron:
            TheLibrary.removePatron(patron)
        else:
            print("Patron not found.")

    elif Userwant == "BORROW BOOK":
        title = input("Please enter the title: ")
        book = next((b for b in TheLibrary.books if b.title == title), None)
        if book:
            TheLibrary.borrowBook(book)
        else:
            print("Book not found.")

    elif Userwant == "RETURN BOOK":
        title = input("Please enter the title: ")
        book = next((b for b in TheLibrary.books if b.title == title), None)
        if book:
            TheLibrary.returnBook(book)
        else:
            pages = input("Please enter the number of pages: ")
            genre = input("Please enter the genre: ")
            author = input("Please enter the author: ")
            isbn = input("Please enter the ISBN code: ")
            borrowed = True
            newBook = Books(title, pages, genre, author, isbn, borrowed)
            TheLibrary.returnBook(newBook)

    elif Userwant == "LIST BOOKS":
        for book in TheLibrary.listBooks():
            print(book)

    elif Userwant == "LIST PATRONS":
        for patron in TheLibrary.listPatrons():
            print(patron)

    elif Userwant == "LIST LIBRARIANS":
        for librarian in TheLibrary.listLibrarians():
            print(librarian)

    elif Userwant == "END":
        print("Thank you for using my aplication have a good day :)")
        break

    else:
        print("Invalid action. Please try again.")

    time.sleep(1)
