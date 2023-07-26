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

#REGISTRAR BIBLIOTECA
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


#MODIFICAR LIBRO
def modify_book(book, your_library):
    clear_window()
    
    
    while True:
        clear_window()
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tModificar Libro:")
        
        print(f"Titulo anterior: {book.title}")
        new_title = input("Nuevo titulo: ")
        while not new_title:  new_title = input()

        print(f"Autor anterior: {book.author}")
        new_author = input("Nuevo autor: ")
        while not new_author:  new_author = input()

        print(f"Condición anterior: {book.condition}")
        print("Seleccione nueva condición:\n1- Nuevo\n2- Bien\n3- Mal")
        new_condition = input() 
        
        while not new_condition or new_condition not in ["1","2","3"]:
            new_condition = input().strip()
        new_condition = int(new_condition)

        if new_condition == 1:
            new_condition = "Nuevo"
        elif new_condition == 2:
            new_condition = "Bien"
        elif new_condition == 3:
            new_condition = "Mal"

        #Modificando libro
        clear_window()
        print("\tModificado..")
        wait_secons(0.5)
        book.title = new_title
        book.author = new_author
        book.condition = new_condition
        print("\tLibro modificado.")
        wait_secons(2)
        #finaliza modificación

        
        carry_on = show_book(book, your_library)
        if not carry_on: break

#ELIMINAR LIBRO
def delete_book(del_book,your_library):
    clear_window()
    print("Eliminando libro..")

    for book in your_library.books:
        if book.id == del_book.id:
            your_library.remove_book(book)
            break
    else:
        print("No se a podido eliminar, revise el ID.")
        wait_secons(2)
        clear_window()
        return
    print("Libro eliminado.")
    wait_secons(2)
    clear_window()
    return
    
    

#REGISTRAR LIBRO
def register_book(your_library):
    books =[]

    while True:
        title = ""
        author = ""
        condition = ""
        clear_window()
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tRegistrar libro")

        title = input("Titulo: ")
        while not title: title = input("Titulo: ")

        author = input("Autor: ")
        while not author: author = input("Ingrese un autor(desconocido/anónimo)\n Autor: ")

        print("Estado del libro:\n1- Nuevo\n2- Bien\n3- Mal")
        condition = input()
        
        while not condition or int(condition) not in [1,2,3]:
            condition = input().strip()
        condition = int(condition)

        if condition == 1:
            condition = "Nuevo"
        elif condition == 2:
            condition = "Bien"
        elif condition == 3:
            condition = "Mal"
 
        id = 1
        for book in your_library.books:
            if book.id>=id:
                id = book.id + 1

        book = Book(id, title, author, condition)
        your_library.add_book(book)
        books.append(book)
        clear_window()
        #finaliza registro

        #menú para continuar
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tRegistrar libro")
        print("1- Ingresar otro libro \n2- Mostrar libros agregados\n3-Menú principal")
        op = input()

        while not op or op not in ["1","2","3"]:
                op = input().strip()
        op = int(op)

        if op == 1:
            continue
        if op == 2:
            clear_window()
            print("\t\tMostrando libros agregados...")
            wait_secons(1)             
            show_result_menu(books, your_library)
        break

#BUSCAR LIBROS
def search_books(filters, your_library):
    
    if len(your_library.books) == 0:
        clear_window()
        print("\tAun no tienes libros.")
        wait_secons(2)
        return False
    
    books = []

    if filters == "all":
        for book in your_library.books:
            books.append(book)
    elif filters["condition"]:
        for book in your_library.books:
            if book.condition == filters["condition"]:
                books.append(book)
    elif filters["title"] and filters["author"]:
        for book in your_library.books:
            if book.title == filters["title"] and book.author == filters["author"]:
                books.append(book)
    else:
        for book in your_library.books:
            if book.title == filters["title"] or book.author == filters["author"]:
                books.append(book)

    if books: 
        show_result_menu(books, your_library)
    else:
        clear_window()
        print("\t\tNo se han encontrado libros")
        wait_secons(2)
    return False

#BUSCAR POR ID
def search_for_id(id, your_library):
    
    if len(your_library.books) == 0:
        clear_window()
        print("\tAun no tienes libros.")
        wait_secons(2)
        return False
    
    clear_window()
    
    action = search_for_id
    if id == "modificar": action = modify_book; id = ""
    if id == "eliminar": action = delete_book; id = ""

    if not id: 
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tBuscar libro/s:")
        id = input("ID: ").strip()
    
        while not id :
            id = input("ID: ").strip()
        
        while True:
            try:
                id = int(id)
                break
            except:
                print("id debe ser un numero")
                id = input("ID: ").strip()
        
        book = ""
        for book in your_library.books:
            if book.id == id:
                book = book
                break
        action(book, your_library)
        return False

    book = ""
    for book in your_library.books:
        if book.id == id:
            book = book
            break
    if book:
        show_book(book, your_library)
    else:
        print("\t\tNo se encontraron libros con el ID especificado.")
        wait_secons(2)
        return False

#MOSTRAR UN LIBRO
def show_book(book, your_library):
    while True:
        try:
            clear_window()
            print(f"\t\t{your_library}")
            print("\tDetalles del Libro")
            print(f"Titulo del Libro: {book.title}")
            print(f"Autor del Libro: {book.author}")
            print(f"Condición del Libro: {book.condition}")
            print(f"ID: {book.id}")
            print("1- Modificar libro \n2- Volver al menú")
            op = input()
            
            while not op or op not in ["1","2"]:
                    op = input().strip()
            op = int(op)

            if op == 1: op = modify_book(book, your_library)
            break
        except:
            print("\tAh ocurrido un error, vuelva a intentar")
            input("\tPrecione enter para continuar")
            break


#MENU
def show_menu(op, your_library):
    clear_window()
    try:    
        print(f"\t\tBiblioteca {your_library.name}")
        print("\tMenu Principal")
        
        for i, element in enumerate(op):
            print (f"{i+1}- {element} ")

        op = input().strip()

        while not op or op not in [str(numero) for numero in range(1,7)]:
            op = input().strip()
        return int(op)
    
    except:
        error_msg()
        return False
    
#MOSTRAR LIBROS
def show_result_menu(results_search, your_library):
    if len(results_search) == 1:
        show_book(results_search[0], your_library)
        return False
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    print(f"Seleccione un libro si desea modificar:")
    for i, book in enumerate(results_search):
        print(f"{i+1}- {book}")
    print(f"{len(results_search)+1}- Menú principal")
    op = input()
    
    while not op or op not in [str(numero) for numero in range(1,len(results_search)+2)]:
            op = input().strip()
    op = int(op)

    if op == len(results_search)+1:
        return False
    else:
        modify_book(results_search[op-1], your_library)
        return False

#AGREGAR FILTROS    
def add_filters(your_library):
    
    if len(your_library.books) == 0:
        clear_window()
        print("\tAun no tienes libros.")
        wait_secons(2)
        return False
    
    clear_window()
    print(f"\t\tBiblioteca {your_library.name}")
    print("\tFiltros de busqueda")
    print("\tIngrese ID del libro (Si no lo sabe precione enter)")
    
    try:
        id = input("ID: ").strip()

        title = ""
        author = ""
        condition = ""

        if id:
            while True:
                try:
                    id = int(id)
                    break
                except:
                    print("id debe ser un numero")
                    id = input("ID: ").strip()

            return {"title": title, "author": author,"id": id, "condition": condition }
        else:
            title = input("Titulo: ")
            author= input("Autor: ")
            return {"title": title, "author": author,"id": id, "condition": condition }

    except:
        error_msg()   