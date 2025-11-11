from abc import ABC, abstractmethod

class NoAvailableCopies(Exception):
    def __init__(self):
        self.message = "There are no available copies of this object"
        super().__init__(self.message)

class LibraryObject(ABC):
    id_num = 0
    @abstractmethod
    def __init__(self, copies, shelf, title, author, genre, description):
        global id_num
        self.ID = id_num
        id_num += 1

        self.shelf = shelf
        self.copies = copies
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.code = author.substr(author.index(" "), author.index(" ") + 3)


    def check_out(self):
        if self.copies > 0:
            self.copies -= 1
        else:
            raise NoAvailableCopies()

    def check_in(self):
        self.copies += 1

class Book(LibraryObject):
    def __init__(self, copies, shelf, title, author, genre, description, isbn):
        super().__init__(copies, shelf, title, author, genre, description)
        self.genre = genre
        self.isbn = isbn

class NonFictionBook(Book):
    def __init__(self, copies, shelf, title, author, genre, description, isbn, dewey):
        super().__init__(copies, shelf, title, author, genre, description, isbn)
        self.dewey = dewey

class DVD(LibraryObject):
    def __init__(self, copies, shelf, title, writer, description, genre, release_date, production_company, main_actors):
        super().__init__(copies, shelf, title, writer, genre, description)
        self.release_date = release_date
        self.production_company = production_company
        self.main_actors = main_actors

class CD(LibraryObject):
    def __init__(self, copies, shelf, title, band, genre, description, record_label):
        super().__init__(copies, shelf, title, band, genre, description)
        self.record_label = record_label

