# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.autho = author
        
        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))
    

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __srt_(self):
        return f"{self.fname} {self.lname}"

b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
b1.addchapter("Chapter 3", 143)

print(b1.title)
