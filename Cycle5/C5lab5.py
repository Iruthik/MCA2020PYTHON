# 5. Create a class Publisher (name). Derive class Book from Publisher with attributes title  and
# author. Derive class Python from Book with attributes price and no_of_pages. Write   a
# program that displays information about a Python book. Use base class constructor invocation and
# method overriding.


class publisher:
    def __init__(self,name):
        self.name = name
    def myMethod(self):
        print("Name of the publisher:",self.name)
class books(publisher):
    def __init__(self,name,title,author,):
        self.name = name
        self.title = title
        self.author = author

    def myMethod(self):
        print("This is Child(book) class Method override confirm")
        print("Title:",self.title)
        print("Author:",self.author)


class python(books):
    def __init__(self,name,title,author,price,no_of_pages):
        self.name = name
        self.title = title
        self.author = author
        self.price = price
        self.no_of_pages = no_of_pages


    def Display(self):
        print("\n\n\nBOOK DETAILS")
        print("Publisher:",self.name)
        print("Book_Title:",self.title)
        print("Book_Author", self.author)
        print("Pages:", self.no_of_pages)
        print("Price:", self.price)
name = input("Enter Name of Publisher:")
title = input("Enter Title of Book:")
author = input("Enter Author name:")
page = int(input("Enter Number of Pages:"))
price = int(input("Enter Price Of Book:"))
obj = python(name,title,author,page,price)
obj.myMethod()
obj.Display()



