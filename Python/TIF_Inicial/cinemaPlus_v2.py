import os

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
    opcion = input("> ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        opcion = input("¡Se ingreso una opcion no válida! Ingrese una opcion [1-4]\n> ")
    if opcion == "1":
        menu_AMB()
    elif opcion == "2":
        menu_calificacion()
    elif opcion == "3":
        menu_reportes()
    else:
        limpiar_pantalla()
        print("Gracias por ser parte del staff de CINEMA+")        

def menu_AMB():
    limpiar_pantalla()
    print("CINEMA+\nAlta, Baja y modificación de películas\n")
    print("1. Alta de nueva película")
    print("2. Modificación de película existente")
    print("3. Baja de película (eliminar)")
    print("4. Volver")
    opcion = input("> ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        opcion = input("¡Se ingreso una opcion no válida! Ingrese una opcion [1-4]\n> ")
    if opcion == "1":
        alta_pelicula()
    elif opcion == "2":
        modificar_pelicula()
    elif opcion == "3":
        baja_pelicula()
    else:
        menu_princpal()
def alta_pelicula():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("aca se dan de alta las peliculas")
    pausar()
    menu_AMB()
def modificar_pelicula():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("aca se  modifican las peliculas")
    pausar()
    menu_AMB()
def baja_pelicula():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se  eliminan las peliculas")
    pausar()
    menu_AMB()

def menu_calificacion(): #no es menu pero para seguir con la onda de opciones, preguntar criterio
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
    opcion = input("> ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        opcion = input("¡Se ingreso una opcion no válida! Ingrese una opcion [1-4]\n> ")
    if opcion == "1":
        listado_peliculas()
    elif opcion == "2":
        peliculas_mayor_puntaje()
    elif opcion == "3":
        porcentaje_peliculas_disponibles()
    else:
        menu_princpal()
def listado_peliculas():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca va el listado de las peliculas")
    pausar()
    menu_reportes()
def peliculas_mayor_puntaje():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se listan las 15 peliculas mejor calificadas")
    pausar()
    menu_reportes()
def porcentaje_peliculas_disponibles():
    limpiar_pantalla()
    print("CINEMA+\n")
    print("Aca se muestra el histograma de disponibles/no disponibles")
    pausar()
    menu_reportes()

menu_princpal()