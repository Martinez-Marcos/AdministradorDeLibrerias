import Book

class library:
    def __init__ (selft, name = "", location= ""):
        selft.name = name
        selft.location = location
        books = []
    
    @property    
    def name(selft):
        return selft.__name

    @name.setter     
    def name(selft, name):
        selft.__name = name
    
    @property 
    def location(selft):
        return selft.__location

    @location.setter    
    def location(selft, location):
        selft.__location =location 

    @property 
    def books(selft):
        return selft.__books
    
    def receive_book(selft, book):
        selft.books.append(book)

    def discard_book(selft, id):
        for book in selft.books:
            if (book.id == id):
                index = book.index
                selft.books.pop(index)
            


