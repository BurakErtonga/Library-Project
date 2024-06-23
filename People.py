class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id

    def __str__(self):
        return f"Name: {self.name}, ID: {self.librarian_id}"

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id

    def __str__(self):
        return f"Name: {self.name}, ID: {self.patron_id}"
