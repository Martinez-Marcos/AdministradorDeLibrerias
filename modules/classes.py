class Book:

    def __init__(self, id, title, author, condition):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__condition = condition

    @property    
    def id(self):
        return self.__id

    @id.setter     
    def id(self, id):
        self.__id = id
    
    @property    
    def title(self):
        return self.__title

    @title.setter     
    def title(self, title):
        self.__title = title
    
    @property 
    def author(self):
        return self.__author

    @author.setter    
    def author(self, author):
        self.__author =author 

    @property 
    def condition(self):
        return self.__condition

    @condition.setter  
    def condition(self, condition):
        self.__condition = condition
    
    def __str__(self) -> str:
        return f"Titulo: {self.__title} Autor: {self.__author} Condicion: {self.__condition} Id: {self.__id}"

class Library:
    def __init__ (self, name, location):
        self.__name = name
        self.__location = location
        self.__books = []
    
    @property    
    def name(self):
        return self.__name

    @name.setter     
    def name(self, name):
        self.__name = name
    
    @property 
    def location(self):
        return self.__location

    @location.setter    
    def location(self, location):
        self.__location = location
    
    @property 
    def books(self):
        return self.__books
    
    @books.setter
    def add_book(self, book):
        self.__books.append(book)
    
    @books.deleter
    def remove_book(self, book):
        self.__books.remove(book)
    
    def __str__(self):
        return f"Biblioteca {self.name} de {self.location}"