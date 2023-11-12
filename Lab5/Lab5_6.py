'''Lab5 6'''

'''
Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD
and Magazine. Include methods to check out, return, and display information about each item.
'''


class LibraryItem:
    def __init__(self,author,name,price):
        self.author=author
        self.name=name
        self.price=price

class Book(LibraryItem):
    def __init__(self,author,name,price,editure,nrOfPages,description):
        super().__init__(author,name,price)
        self.editure=editure
        self.nrOfPages=nrOfPages
        self.description=description
        self.returned=False

    def CheckOut(self):
        if self.borrowed: return "The book is not avaible"
        return "Book ("+ self.name+ " ) : Very interesting"

    def Borrow(self):
        if(self.returned==False):
            return "This book is already borrowed!"
        self.returned=True

    def Return(self):
        if(self.returned):
            return  "Book already returned"
        self.returned=True

    def __str__(self):
        return ("Book: "+self.name+"\n"+
                "Author: "+self.author+"\n"+
                "Editure:" + self.editure+"\n"+
                "Description: "+self.description+"\n"
                )


class Magazine(LibraryItem):
    def __init__(self,author,name,price,editure,nrOfPages,description):
        super().__init__(author,name,price)
        self.editure=editure
        self.nrOfPages=nrOfPages
        self.description=description
        self.returned=False
        self.borrowed=False

    def Borrow(self):
        if(self.returned==False):
            return "This magazine is already borrowed!"
        self.returned=True

    def Return(self):
        if(self.returned):
            return  "Magazine already returned"
        self.returned=True

    def Return(self):
        if(self.returned):
            return  "Magazine already returned"
        self.returned=1

    def __str__(self):
        return ("Magazine: "+self.name+"\n"+
                "Author: "+self.author+"\n"+
                "Editure:" + self.editure+"\n"+
                "Description: "+self.description+"\n"
                )

class DVD(LibraryItem):
    def __init__(self, author, name, price, size, description):
        super().__init__(author, name, price)
        self.size=size
        self.description = description
        self.returned = False
        self.borrowed = False
    def CheckOut(self):
        if self.borrowed: return "The DVD is not avaible"
        return "DVD ("+ self.name+ " ) : Very interesting"

    def Borrow(self):
        if(self.returned==False):
            return "This DVD is already borrowed!"
        self.returned=True

    def Return(self):
        if(self.returned):
            return  "DVD already returned"
        self.returned=True

    def __str__(self):
        return ("DVD: "+self.name+"\n"+
                "Size: "+str(self.size)+"\n"+
                "Description: "+self.description+"\n"
                )

book=Book("Alexandre Dumas","Vicontele de Bragelonne",40,"Adevarul",2560,"Recomand")
print(book)

dvd=DVD("Blizzard","Warcraft III",0,256,"Recomand")
print(dvd)


