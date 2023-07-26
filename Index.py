#importa clases y funciones internas
from modules import Functions as f
from modules import classes as c




def main():
    # Define Variable y constantes
    exit = False
    op = {
        "Buscar libro/s": 1,
        "Ingresar libro/s": 2,
        "Reposiciones necesarias": 3,
        "Modificar libro": 4,
        "Eliminar libro": 5,
        "Salir": 6
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
    while exit != True:
        opcion = f.show_menu(your_library)
        
        if (opcion == op['Buscar libro/s']):
            try:
                filters = f.add_filters(your_library)
                if filters["id"].strip():
                    id = f.search_for_id(filters["id"], your_library)
                    if id: f.show_book(id, your_library)
                elif filters["author"].strip() or filters["title"].strip():
                    results_search = f.search_books(filters, your_library)
                    if results_search: 
                        id = f.show_result_menu(results_search, your_library)
                        f.show_book(id, your_library)
            except Exception as e:
                print(e)
                f.error_msg()

        elif (opcion == op["Ingresar libro/s"]):
            books = f.register_book(your_library)
            f.clear_window()
            print("\t\tLibros agregados...")
            f.wait_secons(1)
            selection = f.show_result_menu(books, your_library)
            f.show_book(selection, your_library)

        elif (opcion == op["Reposiciones necesarias"]):
            filters = [{ "needReplacement": True }]
            results_search = f.search_books(filters, your_library)
            selection = f.show_result_menu(results_search, your_library)
            
            if (selection == "Back"):
                f.show_book(selection, your_library)

        elif (opcion == op['Modificar libro']):
            id = f.search_for_id(your_library)
            f.modify_book(id, your_library)
            f.show_book(id, your_library)

        elif (opcion == op['Eliminar libro']):
            id = f.search_for_id(your_library)
            f.delete_book(id, your_library)

        elif (opcion == op['Salir']):
            exit = True
        
        else:
            print("Esa opción no esta disponible")
    print("Muchas gracias por elegirnos.")
    print("Cerrando app..")
    f.wait_secons(2)
    f.clear_window()

main()
