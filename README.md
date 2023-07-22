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
``` 
Registro
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

- #### aclaraciones
*Siempre que se termina un proceso con un libro se mostrará el libro a excepción del método Eliminar.*   
---
### Desarrollo del diagrama de flujo

AQUI VA EL DIAGRAMA

# Desarrollo de las pruebas de escritorio

- # Prueba de escritorio : BUSCAR LIBRO
- Request:
  - Parámetros opcionales de :
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

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="121px" height="391px" viewBox="-0.5 -0.5 121 391"><defs/><g><ellipse cx="60" cy="30" rx="60" ry="30" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 30px; margin-left: 1px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;"><font style="font-size: 15px;">Inicio/ Crear biblioteca</font></div></div></div></foreignObject><text x="60" y="34" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">Inicio/ Crear biblio...</text></switch></g><rect x="0" y="330" width="120" height="60" rx="9" ry="9" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>

- ## Prueba de escritorio :
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


- ## Prueba de escritorio :
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


- ## Prueba de escritorio :
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


- ## Prueba de escritorio :
- Request:
  - Parámetro obligatorio de tipo URL:
    - 16 *(tipo: integer. Indica el código del mueble que se requiere eliminar)*
- Response:
  - Código HTTP: **200** *message: 'Registro eliminado'*
  - Código HTTP: **500** *message: Se ha generado un error en el servidor*
- Nota: *Los valores indicados en el ejemplo, son datos esperados en los tests.*
