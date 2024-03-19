import os
import json

with open("max_id.json") as archivo_id:
    id_max = json.load(archivo_id)
max_id = int(id_max["max_id"])
with open("peliculas.json") as archivo_peliculas:
    peliculas = json.load(archivo_peliculas)
lista_peliculas = peliculas["peliculas"]

def limpiar_pantalla():
    os.system("cls")
def pausar():
    os.system("pause")

def menu_princpal():
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
        salir = input("¿Desea finalizar el programa? [S/N]\n> ").lower()
        while salir != "s" and salir != "n":
            salir = input("¡Opcion no válida!\n¿Desea finalizar el programa? [S/N]\n> ").lower()
        if salir == "s":
            limpiar_pantalla()
            peliculas["peliculas"] = lista_peliculas
            with open("peliculas.json", "w") as archivo_peliculas:
                json.dump(peliculas, archivo_peliculas, indent=4)
            id_max["max_id"] = max_id
            with open("max_id.json", "w") as archivo_id:
                json.dump(id_max, archivo_id, indent=4)
            print("Gracias por ser parte del staff de CINEMA+")
            os.system("exit")
        else:
            menu_princpal()        

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
        limpiar_pantalla()
        print("CINEMA+\n")
        print("aca se dan de alta las peliculas")
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
    else:
        print("Eliminar una película existente\n")
    print("1. Buscar por id")
    print("2. Buscar por titulo")
    print("3. Volver")
    eleccion = input("> ")
    while eleccion != "1" and eleccion != "2" and eleccion != "3":
        eleccion = input("¡Se ingreso una opcion no válida! Ingrese una opcion en número[1-3]\n> ")
    if eleccion == "1" and desde_donde == "modificacion":
        buscar_id("modificar")
    elif eleccion == "2" and desde_donde == "modificacion":
        buscar_titulo("modificar")
    elif eleccion == "1" and desde_donde == "baja":
        buscar_id("baja")
    elif eleccion == "2" and desde_donde == "baja":
        buscar_id("baja")    
    else:
        menu_AMB()
def buscar_id(desde_donde):
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se buscan las peliculas por id")
    pausar()
    if desde_donde == "baja":
        menu_buscar("baja")
    else:
        menu_buscar("modificacion")
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

menu_princpal()
