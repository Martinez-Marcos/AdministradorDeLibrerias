#imports de system
import os, time
#importa clases internas
from .classes import Book, Library

#FUNCIONES DE SYSTEMA Y ERRORES
def clear_window():
    if os.name == "posix":
        comand = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        comand = "cls"
    os.system(comand)

def wait_secons(time_def):
    time.sleep(time_def)

def error_msg():
    clear_window()
    print("\t\tAh ocurrido un error, vuelva a intentar")
    input("Precione enter para continuar")

#REGISTRO
def register_library():
    try:
        name = input("Ingrese el nombre de su libreria: ")
        location = input("Ingrese la ubicación de su libreria: ") 
        clear_window()
        while not name or not location:
            print("\t\tDebe completar todos los campos\n")
            name = input("Ingrese el nombre de su libreria: ")
            location = input("Ingrese la ubicación de su libreria: ") 
            clear_window()

        your_library = Library(name, location)
        return { "msg": True, "payload": your_library}
    except:
        error_msg()
        return  { "msg": False }


#FUNCIONES DE MANEJO DE LIBROS
def modify_book(your_library):
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    input("modify book")

def delete_book(your_library):
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    input("delete book")

def register_book(your_library):

    books =[]
    while True:
        title = ""
        author = ""
        condition = ""
        clear_window()
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tRegistrar libro")
        while title.strip()=="" or author.strip()=="" or condition not in ["Nuevo","Bueno","Malo"]:
            title = input("Titulo: ")
            author = input("Autor: ")
            print("Estado del libro:\n1- Nuevo\n2- Bueno\n3- Malo")
            condition = input()
            
            while not condition:
                condition = input().strip()
            condition = int(condition)

            if condition == 1:
                condition = "Nuevo"
            elif condition == 2:
                condition = "Bueno"
            elif condition == 3:
                condition = "Malo"
            else:
                condition = ""

        id = 1 
        for book in your_library.books:
            if book.id>=id:
                id = book.id + 1

        book = Book(id, title, author, condition)
        your_library.books = book
        books.append(book)
        print(books)
        if int(input("1- Ingresar otro libro \n2- Continuar")) == 2:
            break                 
        
    return books


def search_books(filters, your_library):
    books = []
    if filters["title"] and filters["author"]:
        for book in your_library.books:
            if book.title == filters["title"] and book.author == filters["author"]:
                books.push(book)
    else:
        for book in your_library.books:
            if book.title == filters["title"] or book.author == filters["author"]:
                books.push(book)

    if books:
        return books
    else:
        clear_window()
        print("\t\tNo hay libros con ese autor o nombre")
        wait_secons(2)
        return False


def search_for_id(id, your_library):
    clear_window()
    books = [book for book in your_library.books if book.id == id]
    if books:
        return books
    else:
        print("\t\tNo se encontraron libros con el ID especificado.")
        wait_secons(2)
        return False

def show_book(selection, your_library):
    exit = False
    while not exit:
        clear_window()
        print(f"\t\tBiblioteca {your_library.name}")
        found = ""
        for book in your_library.books:
            if book.id == selection:
                found = book
        print(f"Titulo del Libro: {found.title}")
        print(f"Autor del Libro: {found.author}")
        print(f"Condición del Libro: {found.condition}")
        print(f"ID: {found.id}")
        input("show book")

#MENUS Y OTRAS VISTAS
def show_menu(your_library):
    clear_window()
    try:    
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tSeleccione una opción")
        print("1- Buscar Libro")
        print("2- Ingresar libro")
        print("3- Ver Resposiciones necesarias")
        print("4- Modificar libro")
        print("5- Eliminar libro")
        print("6- salir")
        inp = input().strip()
        while not inp:
            inp = input().strip()
        return int(inp)
    except:
        print("Ah ocurrido un error, vuelva a intentar")
        input("Precione enter para continuar")
        return -1

def show_result_menu(results_search, your_library):
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    print(f"\tSeleccione una opción")
    for i, book in enumerate(results_search):
        print(f"{i+1}- Titulo: {book.title} Autor: {book.author} Condición: {book.condition} ID: {book.id}") 
    input(f"{len(results_search)+1}- Volver al menú")
    
def add_filters(your_library):
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    print("Ingrese ID del libro (Si no lo sabe precione enter)")

    title =""
    author=""
    id = input("ID: ")

    if (not id.strip()):
        title = input("Titulo: ")
        author = input("Autor: ")
    
    return {"title": title, "author": author,"id": id}