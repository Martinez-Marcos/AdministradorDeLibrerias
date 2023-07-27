#importa clases y funciones internas
from modules import Functions as f
from modules import classes as c




def main():
    # Define Variable y constantes
    op = {
        "Ver libros": 1,
        "Buscar libro/s": 2,
        "Ingresar libro/s": 3,
        "Reposiciones necesarias": 4,
        "Modificar libro": 5,
        "Eliminar libro": 6,
        "Salir": 7
    }
    f.clear_window()
    print("\t\tBienvenido a S.C.B. (Sistema de Control para Bibliotecas)\n")
    
    #Inicia Registro
    print('\tVamos a registrar su biblioteca')
    register =  f.register_library()

    while not register["msg"]:
        f.error_msg()
        register = f.register_library()

    your_library = register["payload"]
    print('\tRegistro completado')
    f.wait_secons(1)

    # Ingresa a Menú
    while True:
        opcion = f.show_menu(op, your_library)

        if (opcion == op["Ver libros"]):
            f.search_books("all",your_library)
            
        elif (opcion == op['Buscar libro/s']):
            filters = f.add_filters(your_library)

            if filters and filters["id"]:
                f.search_for_id(filters["id"], your_library)
            elif filters and (filters["author"].strip() or filters["title"].strip()):
                f.search_books(filters, your_library)

        elif (opcion == op["Ingresar libro/s"]):
            f.register_book(your_library)

        elif (opcion == op["Reposiciones necesarias"]):
            filters= {"condition":"Mal"}
            f.search_books(filters, your_library)

        elif (opcion == op['Modificar libro']):
            f.search_for_id("modificar", your_library)

        elif (opcion == op['Eliminar libro']):
            f.search_for_id("eliminar", your_library)

        elif (opcion == op['Salir']):
            break
        
        else:
            print("Esa opción no esta disponible")
    print("Muchas gracias por elegirnos.")
    print("Cerrando app..")
    f.wait_secons(2)
    f.clear_window()

main()
