class Books:
    def __init__(self, title, pages, genre, author, isbn, borrowed):
        self.title = title
        self.pages = pages
        self.genre = genre
        self.author = author
        self.isbn = isbn
        self.borrowed = borrowed

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Borrowed: {self.borrowed}"
