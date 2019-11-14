#Q1:
class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

class science_Section(Library):
    def __init__(self, book, shelf,name):
        super().__init__(self, book, shelf)
        self.name = name


library1 = Library(300,45)
sc1 = science_Section(300, 45, "Physics books")
print(sc1)
sc1.shelf=4
sc1.book=20
print(sc1.book,sc1.shelf)


