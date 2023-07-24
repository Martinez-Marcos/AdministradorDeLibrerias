#importar funciones
import function.register_library as register_library
import function.show_menu as show_menu
import function.add_filters as add_filters
import function.search_books as search_books
import function.show_result_menu as show_result_menu
import function.show_book_menu as show_book_menu
import function.register_book as register_book
import function.search_for_id as search_for_id
import function.modify_book as modify_book
import function.delete_book as delete_book

# Variable y constantes
exit = False
op = {
    "Buscar libro/s": 1,
    "Ingresar libro": 2,
    "Reposiciones necesarias": 3,
    "Modificar libro": 4,
    "Eliminar libro": 5,
    "Salir": 6
}

def main():
    print('Bienvenido a S.C.B. (Sistema de Control para Bibliotecas)')
    print('Vamos a registrar su biblioteca')
    register = register_library()

    while register != True:
        print('Debe completar todos los campos.')
        register = register_library()
    print('Registro completado')

    
    while exit != True:
        opcion = show_menu()

        if (opcion == op['Buscar libro/s']):
            filters = add_filters()
            results_search = search_books(**filters)
            selection = show_result_menu(results_search)

            if (selection == 'Back'):
                show_book_menu(selection)

        elif (opcion == op['Ingresar libro']):
            book = register_book()
            show_book_menu(book.id)

        elif (opcion == op['Reposiciones necesarias']):
            filters = [{ "needReplacement": True }]
            results_search = search_books(**filters)
            selection = show_result_menu(results_search)
            
            if (selection == 'Back'):
                show_book_menu(selection)

        elif (opcion == op['Modificar libro']):
            id = search_for_id()
            modify_book(id)
            show_book_menu(id)

        elif (opcion == op['Eliminar libro']):
            id = search_for_id()
            delete_book(id)

        elif (opcion == op['Salir']):
            exit = True
        
        else:
            print("Esa opción no esta disponible")
    print("Muchas gracias por elegirnos.")
print("Cerrando app..")
