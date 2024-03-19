from json import load, dump
from random import randint
import os


lista_peliculas = []
peliculas_eliminadas = []
id_max = None
opc_menu_principal = ("ABM películas", "Calificación de películas", "Reportes y estadistica", "Salir")
opc_menu_abm = ("Alta de nueva película", "Modificación de película existente", "Baja de película (Eliminar)", "Volver")
opc_menu_reporte = ("Listado de películas", "Películas de mayor puntaje", "Porcentaje de películas disponibles en la plataforma", "Volver")
opc_menu_buscar = ("Buscar por ID", "Buscar por título", "Volver")
dicc_pelicula = {}
indices_buscar_pelicula = []
titulos_buscar_pelicula =[]


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_datos():
    global lista_peliculas
    with open("peliculas.json") as archivo:
        lista_peliculas = load(archivo)
    global peliculas_eliminadas
    with open("peliculas_eliminadas.json") as archivo:    
        peliculas_eliminadas = load(archivo)
    global id_max
    with open("max_id.json") as archivo:
        id_max = load(archivo)

def guardar():
    with open("peliculas.json", "w") as archivo_guardar:
      dump(lista_peliculas, archivo_guardar, indent=4)
    with open("max_id.json", "w") as archivo_guardar:
      dump(id_max, archivo_guardar, indent=4)
    with open("peliculas_eliminadas.json", "w") as archivo_guardar:
      dump(peliculas_eliminadas, archivo_guardar, indent=4)
    cargar_datos()

def mostrar_opciones(opciones_a_mostrar):
    for x in range(0, len(opciones_a_mostrar)):
        print(f"[{x + 1}] - {opciones_a_mostrar[x]}" )

def mostrar_pelicula(dicc_pelicula_mostrar): #TODO: ver como mostrar los booleanos como si o no
    for x, y in dicc_pelicula_mostrar.items():
        print(x.ljust(13) + ": " + str(y))

def imprimir_menu_principal():
    while True:
        limpiar_pantalla()
        print("CINEMA+\n")
        mostrar_opciones(opc_menu_principal)
        opcion = input("> ")
        while not opcion.isnumeric() or int(opcion) not in range(1, len(opc_menu_principal)+1):
            opcion = input(f"¡Opción No valida! Ingrese nuevamente una opción[1-{len(opc_menu_principal)}]> ")
        if opcion == "1":
            imprimir_menu_abm() 
        elif opcion == "2":
            calificar_pelicula()
        elif opcion == "3":
            imprimir_menu_reportes()
        elif opcion == "4":
            limpiar_pantalla()
            salir = input("CINEMA+\n\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            while salir != "s" and salir != "n":
                salir = input("¡Opcion no válida!\n¿Desea finalizar el programa? [S/N]\n> ").lower()
            if salir == "s":
                limpiar_pantalla()
                print("CINEMA+\n\n¡Gracias por ser parte de nuestro staff!")
                guardar()
                break

def imprimir_menu_abm():
    while True:
        dicc_pelicula.clear()
        limpiar_pantalla()
        indice = None
        print("CINEMA+\nAlta, Baja y modificación de películas\n")
        mostrar_opciones(opc_menu_abm)
        opcion = input("> ")
        while not opcion.isnumeric() or int(opcion) not in range(1, len(opc_menu_abm)+1):
            opcion = input(f"¡Opción No valida! Ingrese nuevamente una opción[1-{len(opc_menu_abm)}]\n> ")
        if opcion == "1":
            cargar_pelicula()
        elif opcion == "2" or opcion == "3":
            indice = imprimir_menu_buscar()
            if indice != None:
                if opcion == "2":
                    modificar_pelicula(indice)
                elif opcion == "3":
                    eliminar_pelicula(indice)
        elif opcion == "4":
            break

def calificar_pelicula():
    global dicc_pelicula
    indices_modificados = []
    for pelicula in range(0, 10):
        indice = randint(0, (len(lista_peliculas)-1))
        while indice in indices_modificados:
            indice = randint(0, (len(lista_peliculas)-1))
        indices_modificados.append(indice)
        dicc_pelicula = lista_peliculas[indice]
        limpiar_pantalla()
        print("CINEMA+\nCalificacion de películas\n")
        mostrar_pelicula(dicc_pelicula)
        print(f"\nPelicula {pelicula + 1}/10 a calificar:")
        calificar = input("¿Desea calificar la película? [S/N]\n> ").lower()
        while calificar != "s" and calificar != "n":
            calificar = input("¡Ingreso una opción no valida! Debe ser \"S\" para si o \"N\" para no\n¿Desea calificar la pelicula? [S/N]\n> ").lower()
        if calificar == "s":
            calificacion = input("Califique la pelicula en numero [1-10]\n> ")
            while not calificacion.isnumeric() or int(calificacion) < 1 or int(calificacion) > 10:
                calificacion = input("¡Calificacion no válida! Ingrese un número del 1 al 10 para calificar la película\n> ")
            if dicc_pelicula["calificacion"] == None:
                dicc_pelicula["calificacion"] = int(calificacion)
            else:
                dicc_pelicula["calificacion"] = (dicc_pelicula["calificacion"] + int(calificacion)) / 2
                print(f"La nueva calificación de la pelicula es {dicc_pelicula['calificacion']}")
                lista_peliculas[indice] = dicc_pelicula
                guardar()
    pausa = input("Presione enter para continuar...")

def imprimir_menu_reportes():
    while True:
        limpiar_pantalla()
        print("CINEMA+\nReportes y estadísticas\n")
        mostrar_opciones(opc_menu_reporte)
        opcion = input("> ")
        while not opcion.isnumeric() or int(opcion) not in range(1, len(opc_menu_reporte)+1):
            opcion = input(f"¡Opción No valida! Ingrese nuevamente una opción[1-{len(opc_menu_reporte)}]\n> ")
        if opcion == "1":
            listar_peliculas_titulo(lista_peliculas)
        elif opcion == "2":
            listar_peliculas_top(lista_peliculas)
        elif opcion == "3":
            mostrar_histograma()
        elif opcion == "4":
            break

def imprimir_menu_buscar():
    while True:
        indice = None
        limpiar_pantalla()
        print("CINEMA+\n")
        mostrar_opciones(opc_menu_buscar)
        opcion = input("> ")
        while not opcion.isnumeric() or int(opcion) not in range(1, len(opc_menu_buscar)+1):
            opcion = input(f"¡Opción No valida! Ingrese nuevamente una opción[1-{len(opc_menu_buscar)}]\n> ")
        if opcion == "1":
            indice = buscar_id() 
            return indice
        elif opcion == "2":
            indice = buscar_titulo()
            return indice
        elif opcion == "3":
            break

def buscar_id():
    while True:
        limpiar_pantalla()
        print("CINEMA+\nBuscar película por ID\n")
        while True:
            busqueda = input("Ingrese el ID de la pelicula\n> ")
            if not busqueda.isnumeric():
                print("¡Opcion no valida! Debe ingresar un numero")
            else:
                break
        for pelicula in range(0, len(lista_peliculas)): #TODO: Ver si es mejor modificar la variable pelicula a indice_pelicula
            if lista_peliculas[pelicula]["id"] == int(busqueda):
                return pelicula #Retorna el indice de la pelicula en lista_peliculas
        else:
            repetir_busqueda = input("¡El id ingresado no existe!\n¿Desea realizar otra busqueda? [S/N]\n> ")
            while repetir_busqueda != "s" and repetir_busqueda != "n":
                repetir_busqueda = input("¡Opción ingresada no válida!\n¿Desea realizar otra busqueda? [S/N]\> ")
            if repetir_busqueda.lower() == "n":
                break
             
def buscar_titulo():
    buscar = True 
    while buscar:
        indices_buscar_pelicula.clear()
        titulos_buscar_pelicula.clear()
        limpiar_pantalla()
        print("CINEMA+\nBuscar película por Titulo\n")
        while True:
            busqueda = input("Ingrese el titulo de la película\> ")
            if busqueda == "":
                print("¡Debe ingresar un titulo o palabra a buscar!")
            else:
                break
        for pelicula in range(0, len(lista_peliculas)):#pelicula es el indice 
            if busqueda.lower() in lista_peliculas[pelicula]["titulo"].lower():  # generamos dos listas una para los indices y la otra para el titulo
                indices_buscar_pelicula.append(pelicula)
                titulos_buscar_pelicula.append(lista_peliculas[pelicula]["titulo"])
        mostrar_opciones(titulos_buscar_pelicula)      
        if len(indices_buscar_pelicula) == 0:
            print("No se encontraron coincidencias")
            while True:
                buscar_otra = input("¿Desea realizar otra búsqueda? [S/N]\n> ") 
                if buscar_otra != "s" and buscar_otra != "n":
                    print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")
                else:
                    break
            if buscar_otra.lower() == "n":
                buscar = False
                break
            elif buscar_otra.lower() == "s":
                continue
        else:
            opcion = input("Si encontró la película buscada ingrese el numero de opción, de lo contrario ingrese \"N\"\n> ")
            while True:
                if opcion.isnumeric() and int(opcion) in range(1, len(indices_buscar_pelicula)+1):
                    return indices_buscar_pelicula[int(opcion)-1]
                elif opcion.lower() == "n":
                    buscar_otra = input("¿Desea realizar otra búsqueda? [S/N]\n> ")
                    while buscar_otra != "s" and buscar_otra != "n": 
                        buscar_otra = input("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no\n> ")
                    if buscar_otra.lower() == "n":
                        buscar = False
                        break
                    elif buscar_otra.lower() == "s":
                        break
                else:
                    opcion = input("¡Opción ingresada no válida!\n Si encontró la película buscada ingrese el numero de opción, de lo contrario ingrese \"N\"\n> ")
         
def eliminar_pelicula(indice):
    limpiar_pantalla()
    print("CINEMA+\nEliminar película existente\n")
    global dicc_pelicula
    dicc_pelicula = lista_peliculas[indice]
    mostrar_pelicula(dicc_pelicula)
    confirmar = input(f"¿Confirma que desea eliminar la película {lista_peliculas[indice]['titulo']}? [S/N]\n> ")
    while confirmar != "s" and confirmar != "n":
        confirmar = input("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no\n> ")
    if confirmar == "s":
        peliculas_eliminadas.append(lista_peliculas[indice])
        lista_peliculas.pop(indice)
        guardar() 
        print("Se eliminó la película")
        pausa = input("Presione enter para continuar...")
    else:
        guardar() 

def mostrar_histograma():
    limpiar_pantalla()
    print("CINEMA+\nPorcentaje de películas disponibles en la plataforma\n")
    disponibles = 0
    no_disponibles = 0
    for pelicula in lista_peliculas:
        if pelicula["disponible"] == True:
            disponibles += 1
        else:
            no_disponibles += 1
    total_peliculas = disponibles + no_disponibles
    porcentaje_disponibles = round((disponibles / total_peliculas) * 100, 2)
    porcentaje_no_disponibles = round((no_disponibles / total_peliculas) * 100, 2)
    print("Disponibles".ljust(14) + "|" + ("*" * round(porcentaje_disponibles/10)).ljust(11) + "|" + str(porcentaje_disponibles) + "%")
    print("No Disponibles" + "|" + ("*" * round(porcentaje_no_disponibles/10)).ljust(11) + "|" + str(porcentaje_no_disponibles) + "%")
    pausa = input("Para salir presione Enter...")
    
def cargar_pelicula():
    agregar = True
    while agregar:
        dicc_pelicula.clear()
        print("CINEMA+\nCargar nueva película\n")
        dicc_pelicula["id"] = agregar_id()
        dicc_pelicula["titulo"] = agregar_valor_str("titulo")
        dicc_pelicula["genero"] = agregar_generos() 
        dicc_pelicula["duracion"] = agregar_duracion()
        dicc_pelicula["sinopsis"] = agregar_valor_str("sinopsis")
        dicc_pelicula["pais"] = agregar_valor_str("pais de origen")
        dicc_pelicula["idioma"] = agregar_valor_str("idioma")
        dicc_pelicula["clasificacion"] = agregar_clasificacion()
        dicc_pelicula["calificacion"] = None
        dicc_pelicula["disponible"] = agregar_disponibilidad()
        limpiar_pantalla()
        print("CINEMA+\nCargar nueva película\n")
        mostrar_pelicula(dicc_pelicula)
        while True:
            guardar_alta = input("¿Desea agregar la pelicula? [S/N]\n> ")
            if guardar_alta.lower() == "s":
                 lista_peliculas.append(dicc_pelicula)
                 guardar()
                 print("¡Película agregada con éxito!")
                 pause = input("Presione enter para continuar...")
                 break
            elif guardar_alta.lower() == "n":
                 break
            else:
                 print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")
        limpiar_pantalla()
        print("CINEMA+\nCargar nueva película\n")
        while True:
            agregar_otra = input("¿Desea agregar otra película? [S/N]\n> ")
            if agregar_otra.lower() == "s":
                break
            elif agregar_otra.lower() == "n":
                agregar = False
                break
            else:
                print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")

def modificar_pelicula(indice_lista_pelicula):
    limpiar_pantalla()
    print("CINEMA+\nModificar película exitente\n")
    for x, y in lista_peliculas[indice_lista_pelicula].items():
        if x == "id" or x == "calificacion":
            dicc_pelicula[x] = y
            continue
        print(f"{x.ljust(14)}: {y}")
        modificar = input (f"Desea modificar {x}? [S/N]\n> ")
        while modificar.lower() != "n" and modificar.lower() != "s":
            modificar = input("Opción inválida, ingrese S/N\n> ")
        if modificar.lower() == "s":
            if x == "titulo" or x == "sinopsis" or x == "pais" or x == "idioma":
                dicc_pelicula[x] = agregar_valor_str(x)
            elif x == "genero":
                dicc_pelicula[x] = agregar_generos()
            elif x == "duracion":
                dicc_pelicula[x] = agregar_duracion()
            elif x == "clasificacion":
                dicc_pelicula[x] = agregar_clasificacion()
            elif x == "disponible":
                dicc_pelicula[x] = agregar_disponibilidad()
        else:
            dicc_pelicula[x] = y
    limpiar_pantalla()
    print("CINEMA+\nModificar película exitente\n")
    print("Pelicula sin modificar:")
    mostrar_pelicula(lista_peliculas[indice_lista_pelicula])
    print("\nPelicula modificada:")
    mostrar_pelicula(dicc_pelicula)
    while True:
        guardar_cambios = input("\n¿Desea guardar los cambios añadidos a la película? [S/N]\n> ")
        if guardar_cambios == "" or guardar_cambios not in "ns":      
            print("¡Opción no válida! Debe ingresar \"S\" por si o \"N\" por no\n> ")
        else:
            break 
    if guardar_cambios.lower() == "s":
        lista_peliculas[indice_lista_pelicula] = dicc_pelicula
        guardar()
        print("Película modificada con éxito")
        pausa = input("Presione enter para continuar...")

def agregar_id(): 
    global id_max
    id_max += 1
    return id_max

def agregar_valor_str(clave):# titulo, sinopsis, pais e idioma
    limpiar_pantalla()
    print("CINEMA+\nCargar/Modificar película\n")
    mostrar_pelicula(dicc_pelicula)
    valor = input(f"Ingrese el {clave} de la pelicula\n> ")
    while valor == "":
        valor = input(f"¡El Atributo no puede quedar vacío!\nIngrese el {clave} de la pelicula\n> ")
    return valor

def agregar_generos():
    generos = []
    while True:
        limpiar_pantalla()
        print("CINEMA+\nCargar/Modificar película\n")
        mostrar_pelicula(dicc_pelicula)
        print("Ingrese el genero de la película:")
        lista_generos = ["Acción","Animación","Comedia","Drama","Ciencia Ficción","Terror","Suspenso","Romántica"]
        mostrar_opciones(lista_generos)
        if len(generos) > 0:
            print(f"Genero añadidos: {generos}")
        opcion_genero = input("> ")
        if not opcion_genero.isnumeric():
            print("¡Opcion no válida! Debe ingresar un número")
        elif int(opcion_genero) not in range(1, len(lista_generos)):
            print(f"¡Opcion no valida! Debe ingresar un numero 1 al {len(lista_generos)}")
        elif lista_generos[int(opcion_genero) - 1] in generos:
            print("¡El genero ingresado ya esta cargado!")
        else:
            generos.append(lista_generos[int(opcion_genero) - 1])
        print(f"Genero añadidos: {generos}")
        otro = input ("Desea ingresar otro género (S/N)?\n>").lower()
        while otro != "n" and otro != "s":
            otro=input("Opción inválida, ingrese S/N\n> ").lower()
        if otro == "n":
            return generos

def agregar_duracion():
    limpiar_pantalla()
    print("CINEMA+\nCargar/Modificar película\n")
    mostrar_pelicula(dicc_pelicula)
    print("Ingrese duración de la película en minutos")
    duracion = input("> ")
    while duracion < "0" or not duracion.isnumeric():
      print ("Ingrese valor numérico mayor a 0(cero)")
      duracion = input("> ")  
    else:
      return int(duracion) 

def agregar_clasificacion():
    limpiar_pantalla()
    print("CINEMA+\nCargar/Modificar película\n")
    mostrar_pelicula(dicc_pelicula)
    print("Listado de clasificaciones disponibles")
    lista_clasificacion = ["ATP","PG","PG-13","R","NC-17"]
    mostrar_opciones(lista_clasificacion)
    while True:
        opcion_clasificacion = input("Ingrese clasificación de la película\n> ")
        if not opcion_clasificacion.isnumeric() :
          print("¡Opcion no válida! Debe ingresar un número")
        else:
          if int(opcion_clasificacion) not in range(1, len(lista_clasificacion)):
             print(f"¡Opcion no valida! Debe ingresar un numero 1 al {len(lista_clasificacion)}")
          else:
             return lista_clasificacion[int(opcion_clasificacion)-1]

def agregar_disponibilidad():
    limpiar_pantalla()
    print("CINEMA+\nCargar/Modificar película\n")
    mostrar_pelicula(dicc_pelicula)
    disponible = input("Ingrese disponibilidad en streaming (S/N)\n> ").lower()
    while disponible != "s" and disponible != "n":
        disponible = input("Opcion inválida, ingrese (S/N)\n>").lower()
    if disponible == "s": 
        return True
    elif disponible == "n":
        return False 

#TODO: dar formato a los listados, jutificarlos a la izquierda y darles una longitud para que sea mas parecido a una tabla
def listar_peliculas_titulo(lista_peliculas):
    limpiar_pantalla()
    print("CINEMA+")
    print("Listado de películas por Título, géneros y calificación:\n")
    peliculas_ordenadas = sorted(lista_peliculas, key=lambda pelicula: pelicula['titulo'].lower())
    for pelicula in peliculas_ordenadas:
        print(f"Titulo: {pelicula['titulo']} - Genero: {pelicula['genero']} - Calificacion: {pelicula['calificacion']}")
    pausa = input("Presione enter para continuar...")

def listar_peliculas_top(lista_peliculas):
    limpiar_pantalla()
    print("CINEMA+")
    print("Listado de películas con mayor puntaje, TOP 15: \n") 
    lista_peliculas_calificadas = []
    for x in range(0, len(lista_peliculas)):
        if lista_peliculas[x]["calificacion"] != None:
            lista_peliculas_calificadas.append(lista_peliculas[x])
    peliculas_ordenadas = sorted(lista_peliculas_calificadas, key=lambda pelicula: pelicula['calificacion'], reverse=True)
    for pelicula in peliculas_ordenadas[:15]:
        print(f"Titulo: {pelicula['titulo']} - Genero: {pelicula['genero']} - Calificacion: {pelicula['calificacion']}")
    pausa = input("Presione enter para continuar...")

cargar_datos()
imprimir_menu_principal()