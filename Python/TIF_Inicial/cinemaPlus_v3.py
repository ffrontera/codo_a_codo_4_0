import json
import os

#TODO: cargar jSON
#TODO: generar variables lista_peliculas, max_id y peliculas_eliminadas desde el diccionario de json

def limpiar_pantalla():
    os.system("cls")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("CINEMA+\n")
        print("1. ABM de películas")
        print("2. Calificación de títulos")
        print("3. Reportes y estadísticas")
        print("4. Salir\n")
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
        if opcion == "1":
            menu_AMB() 
        elif opcion == "2":
            calificacion()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "4":
            limpiar_pantalla()
            salir = input("CINEMA+\n\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            while salir != "s" and salir != "n":
                salir = input("¡Opcion no válida!\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            if salir == "s":
                limpiar_pantalla()
                print("CINEMA+\n¡Gracias por ser parte de nuestro staff!")
                #TODO: guardar peliculas cargadas, peliculas eliminadas y ultimo id en jSON
                exit()

def menu_AMB():
    while True:
        limpiar_pantalla()
        print("CINEMA+\nAlta, Baja y modificación de películas\n")
        print("1. Alta de nueva película")
        print("2. Modificación de película existente")
        print("3. Baja de película (eliminar)")
        print("4. Volver\n")
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
        if opcion == "1":
            alta_modificacion("alta")
        elif opcion == "2":
            menu_buscar("modificacion")
        elif opcion == "3":
            menu_buscar("baja")
        elif opcion == "4":
            return

def calificacion():
    #TODO: iterar 10 peliculas al azar listando la ficha completa de cada pelicula.
    limpiar_pantalla()
    print("CINEMA+\nCalificacion de titulos\n")
    print("Acá se califican las películas")
    os.system("pause")

def menu_reportes():
    while True:
        limpiar_pantalla()
        print("CINEMA+\nReportes y estadísticas\n")
        print("1. Listado de películas")
        print("2. Películas de mayor puntaje")
        print("3. Porcentaje de películas disponibles en la plataforma")
        print("4. Volver\n")
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
        if opcion == "1":
            listado_peliculas("por titulo")
        elif opcion == "2":
            listado_peliculas("mayor puntaje")
        elif opcion == "3":
            histograma()
        elif opcion == "4":
            return

def menu_buscar(desde_donde):
    while True:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente\n")
        elif desde_donde == "baja":
            print("Eliminar una película existente\n")
        print("1. Buscar por id")
        print("2. Buscar por titulo")
        print("3. Volver\n")
        opcion = input("> ")
        while opcion not in "123":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-3]\n> ")
        if opcion == "1":
            buscar_id(desde_donde) 
        elif opcion == "2":
            buscar_titulo(desde_donde)
        elif opcion == "3":
            return

def buscar_id(desde_donde):
    limpiar_pantalla()
    print("CINEMA+")
    if desde_donde == "modificacion":
        print("Modificar película existente")
    elif desde_donde == "baja":
        print("Eliminar película existente")
    print("Buscar por ID\n")
    busqueda = input("Ingrese el ID de la pelicula: ")
    #while not busqueda.isnumeric(): TODO: revisar por que se clava
     #   busqueda = "¡ID No válido! Debe ingresar un número: "
    #TODO: realizar busqueda, condicional si el id no existe mostrar en pantalla
    if desde_donde == "modificacion":
        alta_modificacion("modificacion")
    elif desde_donde == "baja":
        eliminar() #TODO: agregar el indice de la pelicula a eliminar
    return

def buscar_titulo(desde_donde):
    while True:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente")
        elif desde_donde == "baja":
            print("Eliminar película existente")
        print("Buscar por Titulo\n")
        busqueda = input("Ingrese el titulo de la película: ")
        #TODO: realizar busqueda, condicional si no existe avisar
        if busqueda == "coincidencia": #TODO: generar condicion si la pelicula existe
            if desde_donde == "modificacion":
                alta_modificacion("modificacion")
                return
            elif desde_donde == "baja":
                eliminar() #TODO: agregar el indice al argumento
                return
        else:
            print("¡No hay coincidencias para su busqueda!")
            os.system("pause")
    

def eliminar(): #TODO: agregar indice como parametro
    limpiar_pantalla()
    print("CINEMA+\nEliminar película existente\n")
    print("aca se muestra la ficha completa de la película")#TODO: mostrar ficha completa de la pelicula
    confirmar = ""
    while confirmar != "s" and confirmar != "n":
        confirmar = input("¡Confirma que desea eliminar la película? [S/N]: ")
    if confirmar == "s":
        #TODO: cargar pelicula a lista de eliminadas, eliminar pelicula de la lista
        print("Se elimina la película")
        os.system("pause") 
    return

def histograma(): #TODO: crear función real para histograma
    limpiar_pantalla()
    print("CINEMA+\nPorcentaje de películas disponibles en la plataforma\n")
    print("Disponibles".ljust(14) + "|" + "*"*8)
    print("No Disponibles" + "|" + "*"*2)
    os.system("pause")

def alta_modificacion(desde_donde):
    limpiar_pantalla()
    print("CINEMA+")
    if desde_donde == "alta":
        print("Alta de nueva película\n")
    elif desde_donde == "modificacion":
        print("Modificacion de película existente\n")
    os.system("pause")
    #TODO: alta y la modificacion de películas
    return

def listado_peliculas(como):
    limpiar_pantalla()
    print("CINEMA+")
    if como == "por titulo":
        print("Listado de películas\n")
    elif como == "mayor puntaje":
        print("Las 15 peliculas mejor puntuadas\n")
    print("opcion para volver al menu reportes")
    os.system("pause")
    return


menu_principal()