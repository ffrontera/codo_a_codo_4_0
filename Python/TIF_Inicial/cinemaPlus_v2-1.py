import os
import json

with open("peliculas.json") as archivo_peliculas:
    peliculas = json.load(archivo_peliculas)
lista_peliculas = peliculas["peliculas"]

max_id = peliculas["max_id"]
dicc_pelicula = {}
generos = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
genero = []
clasificacion = ("ATP", "PG", "PG-13", "R", "NC-17")
peliculas_eliminadas = peliculas["peliculas eliminadas"]

def limpiar_pantalla():
    os.system("cls")
def pausar():
    os.system("pause")

def menu_princpal():
    salir = ""
    while salir != "s":
        limpiar_pantalla()
        print("CINEMA+\n")
        print("1. ABM de películas")
        print("2. Calificación de títulos")
        print("3. Reportes y estadísticas")
        print("4. Salir")
        eleccion = input("> ")
        while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
            eleccion = input("¡Se ingreso una opcion no válida! Ingrese una opcion en número[1-4]\n> ")
        if eleccion == "1":
            menu_AMB()
        elif eleccion == "2":
            menu_calificacion()
        elif eleccion == "3":
            menu_reportes()
        else:
            limpiar_pantalla()
            salir = input("CINEMA+\n\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            while salir != "s" and salir != "n":
                salir = input("¡Opcion no válida!\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            if salir == "s":
                limpiar_pantalla()
                peliculas["peliculas"] = lista_peliculas
                peliculas["max_id"] = max_id
                peliculas["peliculas eliminadas"] = peliculas_eliminadas
                with open("peliculas.json", "w") as archivo_peliculas:
                    json.dump(peliculas, archivo_peliculas, indent=4)
                print("CINEMA+\n\nGracias por ser parte de nuestro staff.")
                exit()

def menu_AMB():
    limpiar_pantalla()
    print("CINEMA+\nAlta, Baja y modificación de películas\n")
    print("1. Alta de nueva película")
    print("2. Modificación de película existente")
    print("3. Baja de película (eliminar)")
    print("4. Volver")
    eleccion = input("> ")
    while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
        eleccion = input("¡Se ingreso una opcion no válida! Ingrese una opcion en número[1-4]\n> ")
    if eleccion == "1":
        alta_pelicula()
    elif eleccion == "2":
        menu_buscar("modificacion")
    elif eleccion == "3":
        menu_buscar("baja")
    else:
        menu_princpal()
def alta_pelicula():
    agregar = True
    while agregar:
        global max_id
        limpiar_pantalla()
        dicc_pelicula.clear()
        print("CINEMA+\nAlta de película\n")
        dicc_pelicula["ID"] = max_id + 1
        mostrar_pelicula("alta")
        dicc_pelicula["titulo"] = input("Ingrese el titulo de la pelicula > ")
        while dicc_pelicula["titulo"] == "":
            limpiar_pantalla()
            mostrar_pelicula()
            dicc_pelicula["titulo"] = input("¡Debe ingresar un título! Ingrese el titulo de la pelicula > ")
        sumar_genero = True
        genero.clear()
        mostrar_pelicula("alta")
        while sumar_genero:
            opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
            seleccion_generos(opc_genero)
            otro_genero = ""
            while otro_genero != "s" and otro_genero != "n":
                otro_genero = input(" Desea ingresar otro genero? [S/N] > ").lower()
                mostrar_pelicula("alta")
                print(f"genero       : {genero}")
                if otro_genero == "n":
                    sumar_genero = False
        dicc_pelicula["genero"] = genero
        duracion = ""
        while not duracion.isnumeric():
            mostrar_pelicula("alta")
            duracion = input("Ingrese la duración en minutos de la película ¡En números! > ")
        else:
            dicc_pelicula["duracion"] = int(duracion)
        mostrar_pelicula("alta")    
        sinopsis = input("Ingrese una sinópsis de la pelicula > ")
        while sinopsis == "":
            sinopsis = input("El campo no puede estar vacío\nIngrese una sinópsis de la pelicula > ")
        dicc_pelicula["sinopsis"] = sinopsis
        mostrar_pelicula("alta")
        pais = input("Ingrese el país de origen de la pelicula > ")
        while pais =="":
            pais = input("El campo no puede quedar vácio\nIngrese el país de origen de la pelicula > ")
        dicc_pelicula["pais"] = pais
        mostrar_pelicula("alta")
        idioma = input("Ingrese el idioma de la pelicula > ")
        while idioma == "":
            mostrar_pelicula("alta")
            idioma = input("¡El campo idioma no puede quedar vacío!\nIngrese el idioma de la pelicula > ")
        dicc_pelicula["idioma"] = idioma
        mostrar_pelicula("alta")
        opcion_clasificacion = input("Elija la clasificacion de la pelicula:\n [1]ATP\n [2]PG\n [3]PG-13\n [4]R\n [5]NC-17\n > ")
        while opcion_clasificacion != "1" and opcion_clasificacion != "2" and opcion_clasificacion != "3" and opcion_clasificacion != "4" and opcion_clasificacion != "5":
            mostrar_pelicula("alta")
            opcion_clasificacion = input("!Seleccionó una opción incorrecta!\nElija la clasificacion de la pelicula:\n [1]ATP\n [2]PG\n [3]PG-13\n [4]R\n [5]NC-17\n > ")
        if opcion_clasificacion == "1":
            dicc_pelicula["clasificacion"] = clasificacion[0]
        elif opcion_clasificacion == "2":
            dicc_pelicula["clasificacion"] = clasificacion[1]
        elif opcion_clasificacion == "3":
            dicc_pelicula["clasificacion"] = clasificacion[2]
        elif opcion_clasificacion == "4":
            dicc_pelicula["clasificacion"] = clasificacion[3]
        elif opcion_clasificacion == "5":
            dicc_pelicula["clasificacion"] = clasificacion[4]
        dicc_pelicula["calificacion"] = 0.0
        mostrar_pelicula("alta")
        disponibilidad = input("¿Esta disponible en la plataforma?[S/N] > ").lower()
        while disponibilidad != "s" and disponibilidad != "n":
            disponibilidad = input("!Opción incorrecta!\n¡¿Esta disponible en la plataforma?[S/N] > ")
        if disponibilidad == "s":
            dicc_pelicula["disponible"] = True
        else:
            dicc_pelicula["disponible"] = False
        mostrar_pelicula("alta")
        confirmar = input("¿Confirma que quiere agregar la pelicula?[S/N] >").lower()
        while confirmar != "s" and confirmar != "n":
            confirmar = input("¡Opción incorrecta!\n¿Confirma que quiere agregar la pelicula?[S/N] >").lower()
        if confirmar == "s":
            lista_peliculas.append(dicc_pelicula)
            max_id += 1
        agregar_otra = input("¿Desea agregar otra pelicula? [S/N]\n> ").lower()
        while agregar_otra != "s" and agregar_otra != "n":
            agregar_otra = input("¡Se seleccionó una opcion no válida!\n¿Desea agregar otra pelicula? [S/N]\n>")
        if agregar_otra == "n":
            agregar = False
    menu_AMB()
def menu_buscar(desde_donde):
    limpiar_pantalla()
    print("CINEMA+")
    if desde_donde == "modificacion":
        print("Modificar película existente\n")
    elif desde_donde == "eliminar":
        print("Eliminar película existente\n\"Pelicula eliminada\"")
    else:
        print("Eliminar una película existente\n")
    print("1. Buscar por id")
    print("2. Buscar por titulo")
    print("3. Volver")
    eleccion = input("> ")
    while eleccion != "1" and eleccion != "2" and eleccion != "3":
        eleccion = input("¡Se ingreso una opcion no válida! Ingrese una opcion en número[1-3]\n> ")
    if eleccion == "1" and desde_donde == "modificacion":
        buscar_id("modificacion")
    elif eleccion == "2" and desde_donde == "modificacion":
        buscar_titulo("modificacion")
    elif eleccion == "1" and desde_donde == "baja":
        buscar_id("baja")
    elif eleccion == "2" and desde_donde == "baja":
        buscar_titulo("baja")    
    else:
        menu_AMB()
def buscar_id(desde_donde):
    indice = None
    marcador =False
    while indice == None:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente")
        else:
            print("Eliminar una película existente")
        
        if marcador == False:
            print("Buscar por id\n")
        else:
            print("Buscar por id\n\"El ID no existe\"")
        buscar = int(input("Ingrese el id de la pelicula a buscar > "))
        for id in lista_peliculas:
            if id["ID"] == buscar:
                indice = lista_peliculas.index(id)
                break
        if indice == None:
            marcador = True
        if indice != None:
            for x, y in lista_peliculas[indice].items():
                print(x.ljust(13) + ": " + str(y))    
            if desde_donde == "baja":
                eliminar(indice)
                menu_buscar("baja")
            else:
                menu_buscar("modificacion")
        
def eliminar(indice):
    confirmar = input(f"¿Desea eliminar \"{lista_peliculas[indice]['titulo']}\"?[S/N]>")
    while confirmar != "s" and confirmar != "n":
        confirmar = input(f"¡Opción no válida!\n¿Desea eliminar \"{indice['titulo']}\"?[S/N]>")
    if confirmar == "s":
        peliculas_eliminadas.append(lista_peliculas[indice])
        lista_peliculas.pop(indice)
        menu_buscar("eliminar")
    else:
        menu_buscar("baja")

def buscar_titulo(desde_donde):
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se buscan las peliculas por titulo")
    pausar()
    if desde_donde == "baja":
        menu_buscar("baja")
    else:
        menu_buscar("modificacion")

def menu_calificacion(): #no es menu pero para seguir con la onda de los nombres de las funciones, preguntar criterio
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se califican las peliculas")
    pausar()
    menu_princpal()

def menu_reportes():
    limpiar_pantalla()
    print("CINEMA+\nReportes y estadísticas\n")
    print("1. Listado de películas")
    print("2. Películas de mayor puntaje")
    print("3. Porcentaje de películas disponibles en la plataforma")
    print("4. Volver")
    eleccion = input("> ")
    while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
        eleccion = input("¡Se ingreso una opcion no válida! Ingrese una opcion en número[1-4]\n> ")
    if eleccion == "1":
        listado_peliculas("listado")
    elif eleccion == "2":
        listado_peliculas("calificacion")
    elif eleccion == "3":
        porcentaje_peliculas_disponibles()
    else:
        menu_princpal()
def listado_peliculas(desde_donde):
    limpiar_pantalla()
    print("CINEMA+\n")
    if desde_donde == "listado":
        print("Listado de películas")
        pausar()
    else:
        print("Listado de las 15 películas mejor calificadas")
        pausar()
    menu_reportes()
def porcentaje_peliculas_disponibles():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se muestra el histograma de disponibles/no disponibles")
    pausar()
    menu_reportes()

def seleccion_generos(opc_genero):
    while opc_genero != "1" and opc_genero != "2" and opc_genero != "3" and opc_genero != "4" and opc_genero != "5" and opc_genero != "6" and opc_genero != "7" and opc_genero != "8":
        limpiar_pantalla()
        print("CINEMA+\n")
        print("!Se seleccionó una opción no válida¡")
        opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante:\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
    if generos[int(opc_genero)-1] not in genero:
        if opc_genero == "1":
            genero.append("Acción")
        elif opc_genero == "2":
            genero.append("Animación")
        elif opc_genero == "3":
            genero.append("Comedia")
        elif opc_genero == "4":
            genero.append("Drama")
        elif opc_genero == "5":
            genero.append("Ciencia Ficción")
        elif opc_genero == "6":
            genero.append("Terror")
        elif opc_genero == "7":
            genero.append("Suspenso")
        else:
            genero.append("Romántica")
    else:
        print(f"¡El genero {generos[int(opc_genero)-1]} ya está agregado!")

def mostrar_pelicula(desde_donde):
    limpiar_pantalla()
    if desde_donde == "alta":
        print("\nCINEMA+\nAlta de película\n\nPelicula:")
    for x, y in dicc_pelicula.items():
        print(x.ljust(13) + ": " + str(y))
menu_princpal()
