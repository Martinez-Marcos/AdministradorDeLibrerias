# Proyecto Integral N°2
El presente documento, es el **Proyecto Integral N°2** de la ***Tecnicatura Universitaria en Sistemas Informáticos*** del ***C.U.D.I***. 
- Materia: Programación 2 & Laboratorio 2
- Autores: Pablo Esteban Velazques Montiel, Martinez Marcos

# Necesidad a satisfacer:
A petición de muchos clientes en cuanto a su necesidad de poder controlar sus libros dentro de sus bibliotecas, permitiendoles ver libros disponibles o no disponibles (prestados) además necesitan facilitar el trabajo de recambio dependiendo de su estado y de la compra de libros para su stock. 

# Análisis y solución:
Hemos realizado un análisis de lo necesario dentro del programa (acciones posibles) a saber:
[1] Registrar biblioteca [2] Buscar libro [3] Ingresar Nuevo [4] Ver reposiciones necesarias [5] Modificar libro [6] ELiminar libro. Cada libro tendra un Identificador Único a pesar de tener libros repetidos. Se debe proporcionar el ID del libro al crearlo, junto a sus pertinentes datos, ya que se recomienda estampar de alguna manera en el libro físico.

#### Especificaciones
Esta solución informática sirve registrar los libros de una libreriría. Este programa fue diseñado y construido utilizando los concepto de Programación orientada a objetos, clase, Herencia, Funciones, Ciclos, Bucles, Entrada y control de datos, además, implementa buenas prácticas de programación.

#### Especificaciones técnicas
- Variable de guardado: allBooks
- Tipo de variable: Diccionario
- Interface: Terminal/Interprete de commando

#### Requerimientos
- Python v3.11.4
- GIT v2.40.1
- IDE - Visual Studio Code v1.78.2

#### Estructura del Programa
``` Registro
    └──Petición-datos
        ├── Buscar-Libros
        │   └── Petición-datos
        │        └── Mostrar-resultados
        |             └── Mostrar-libro
        |                 ├── Modificar-libro
        |                 │   └── Petición-datos
        |                 │       └── Confirmar-modificación
        |                 └── Eliminar-libro
        |                     └── Confirmar-eliminación
        ├── Ingresar-libro
        │   └── Petición-datos
        │       └── Mostrar-libro
        |           ├── Modificar-libro
        |           │   └── Petición-datos
        |           │       └── Confirmar-modificación
        |           └── Eliminar-libro
        |               └── Confirmar-eliminación
        ├── Reposiciónes-Necesarias
        │   └── Mostrar-resultados
        |       └──  Mostrar-libro
        |           ├── Modificar-libro
        |           │   └── Petición-datos
        |           │       └── Confirmar-modificación
        |           └── Eliminar-libro
        |               └── Confirmar-eliminación
        ├── Modificar-libro
        │   └── Petición-datos
        │       └── Confirmar-modificación
        └── Eliminar-libro
        |    └── Petición-datos
        |        └── Confirmar-eliminación
        └── Salir
```

 - #### TESTS
    Hasta el momento, hay una sola suite de test (proyecto2.test.js). La misma, se ejecuta por medio del comando ***npm run test***. Para que dicho test pase correctamente, se debe tener una base de datos en MongoDB llamada *muebleria* que tenga una collection denominada *muebles* y esta, contenga los documentos de los muebles. Además, se debe tener el servidor HTTP ejecutandose en otra terminal de Visual Studio Code. Esto se hace con ***npm run start***.

 - #### ERRORES & FORMATOS
    La comprobación de errores y formatos se ejecuta por medio del comando ***npm run eslint***. se hace por medio de Eslint. Para visualizar los errores en tiempo de escritura, se debe tener instalada la extensión de **Eslint** en Visual Studio Code.
    
---
### MÓDULO DE MUEBLES

Este módulo permite la gestión de muebles. El mismo, ofrece funciones para agregar, modificar, borrar o leer el registro de un mueble. Además, permite visualizar reportes filtrados por diferentes criterios de búsqueda.

#### Método GET:
- Request:
  - Parámetros opcionales de tipo QUERY:
    - categoria=Oficina  *(tipo: string. Trae los muebles de una misma categoría)* 
    - precio_gte=500.00  *(tipo: decimal. Trae los muebles que tienen un precio mayor o igual a $500)* 
    - precio_lte=400.00  *(tipo: decimal. Trae los muebles que tienen un precio menor o igual a $400)* 
- Response:
    ``` json
        [
            {
                "_id": "64b082dabbbdbf35047fd6b6",
                "codigo": 7,
                "nombre": "Cama individual",
                "precio": 399.99,
                "categoria": "Dormitorio"
            }
        ]
    ```
  - Código HTTP: **200** *payload: muebles*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*


#### Método GET - Específico:
- Request:
  - Parámetro obligatorio de tipo URL:
    - 9 *(tipo: integer. Indica el código del mueble que se requiere obtener)*
- Response:
    ``` json
        {
              "_id": "64b082dabbbdbf35047fd6b7",
              "codigo": 9,
              "nombre": "Mesa de Comedor de Madera",
              "precio": 299.99,
              "categoria": "Comedor"
        }
    ```
  - Código HTTP: **200** *payload: mueble*
  - Código HTTP: **400** *message: El código no corresponde a un mueble registrado*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*


#### Método POST:
- Request:
  - Parámetros requeridos del BODY:
    - nombre=Biblioteca de madera deluxe *(tipo: string. Establece el valor del nombre)* 
    - precio=1250.55                     *(tipo: integer. Establece el valor del precio)* 
    - categoria=Oficina                  *(tipo: decimal. Establece el valor del categoría)* 
- Response:
  - Código HTTP: **201** *message: 'Registro creado', payload: mueble*
  - Código HTTP: **400** *message: Faltan datos relevantes*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*
- Nota: *Los valores indicados en el ejemplo, son datos esperados en los tests.*


#### Método PUT:
- Request:
  - Parámetro obligatorio de tipo URL:
    - 16 *(tipo: integer. Indica el código del mueble que se requiere modificar)*
  - Parámetros requeridos del BODY:
    - nombre=Modular metálico deluxe *(tipo: string. Establece el valor del nombre)* 
    - precio=999.75                  *(tipo: integer. Establece el valor del precio)* 
    - categoria=Oficina              *(tipo: decimal. Establece el valor del categoría)* 
- Response:
  - Código HTTP: **200** *message: 'Registro actualizado', payload: mueble*
  - Código HTTP: **400** *message: El código no corresponde a un mueble registrado*
  - Código HTTP: **400** *message: Faltan datos relevantes*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*
- Nota: *Los valores indicados en el ejemplo, son datos esperados en los tests.*


#### Método DELETE:
- Request:
  - Parámetro obligatorio de tipo URL:
    - 16 *(tipo: integer. Indica el código del mueble que se requiere eliminar)*
- Response:
  - Código HTTP: **200** *message: 'Registro eliminado'*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*
- Nota: *Los valores indicados en el ejemplo, son datos esperados en los tests.*
