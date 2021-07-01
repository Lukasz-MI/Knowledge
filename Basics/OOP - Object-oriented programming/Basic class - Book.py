class Book:
    def __init__ (self, author, title, ISBN, year):
        self.author = "author: " + author
        self.title = "\ntitle: " + title
        self.ISBN = "\nISBN " + ISBN + ","
        self.year = year
        self.PrintData()

    def PrintData (self):
        print (self.author, self.title, self.ISBN, self.year)

book1 = Book("Kasia" , '"Butterflies"' , "983BCE" , 2018) # Kasia Butterflies 983 BCE 2018



class Book2:
    def __init__ (self, title, author ="unknown", ISBN = "unknown" , year = "unknown"):
        self.author = "author: " + author
        self.title =  "\ntitle: " + title
        self.ISBN = "\nISBN " + ISBN + ","
        self.year = year
        self.Printer()


    def Printer (self):
        print (self.author, self.title, self.ISBN, self.year )


newBook =  Book2 ('"New Horizons"')

newRelease = Book2 ( "Life in France" , author = "Kenny Doug")




