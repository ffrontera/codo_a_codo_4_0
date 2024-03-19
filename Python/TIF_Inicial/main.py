from json import load, dump
from os import system
from random import randint

with open("peliculas.json") as archivo_peliculas: #TODO: acá hay que modificar, tiene que abrir 3 archivos diferentes, peliculas, peliculas_eliminadas y max_id
    lista_peliculas = load(archivo_peliculas)
with open("peliculas.json") as archivo_eliminadas:
    peliculas_eliminadas = load(archivo_eliminadas)
with open("max_id.json") as archivo_id:
    max_id = load(archivo_id)

dicc_pelicula = {}
genero = []
clasificacion = ("ATP", "PG", "PG-13", "R", "NC-17")
generos = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")

def limpiar_pantalla():
    system("cls")

def guardar(): #TODO: hay que separar las listas de peliculas y el max_id en tres archivos diferentes, alguien se anota?
    with open("peliculas.json", "w") as archivo:
        dump(lista_peliculas, archivo, indent=4)
    with open("peliculas_eliminadas.json", "w") as eliminadas:
        dump(peliculas_eliminadas, eliminadas, indent=4)
    with open("max_id.json", "w") as id_max:
        dump(max_id, id_max, indent=4)

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
            menu_ABM() 
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
                print("CINEMA+\n\n¡Gracias por ser parte de nuestro staff!")
                guardar()
                break

def menu_ABM():
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
            alta_pelicula()
        elif opcion == "2":
            menu_buscar("modificacion")
        elif opcion == "3":
            menu_buscar("baja")
        elif opcion == "4":
            break

def calificacion():
    global dicc_pelicula
    indices_modificados = []
    for pelicula in range(0, 10):
        indice = randint(0, (len(lista_peliculas)-1))
        while indice in indices_modificados:
            indice = randint(0, (len(lista_peliculas)-1))
        indices_modificados.append(indice)
        dicc_pelicula = lista_peliculas[indice]
        mostrar_pelicula("calificacion")
        print(f"\nPelicula {pelicula + 1}/10 a calificar:")
        calificar = input("¿Desea calificar la pelicula? [S/N] > ").lower()
        if calificar != "s" and calificar != "n":
            calificar = input("¡Ingreso una opción no valida! Debe ser \"S\" para si o \"N\" para no\n¿Desea calificar la pelicula? [S/N] > ").lower()
        if calificar == "s":
            calificacion = input("Califique la pelicula [1-10],  > ")
            while not calificacion.isnumeric() or int(calificacion) < 1 or int(calificacion) > 10:
                calificacion = input("¡Calificacion no válida! Ingrese un número del 1 al 10 para calificar la película > ")
            if dicc_pelicula["calificacion"] == None:
                dicc_pelicula["calificacion"] = int(calificacion)
            else:
                dicc_pelicula["calificacion"] = (dicc_pelicula["calificacion"] + int(calificacion)) / 2
            print(f"La nueva calificación de la pelicula es {dicc_pelicula['calificacion']}")
            lista_peliculas[indice] = dicc_pelicula
            guardar()
            system("pause")

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
            break

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
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-3]: ")
        if opcion == "1":
            buscar_id(desde_donde) 
        elif opcion == "2":
            buscar_titulo(desde_donde)
        elif opcion == "3":
            break

def buscar_id(desde_donde):
    buscar = True
    while buscar:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente")
        elif desde_donde == "baja":
            print("Eliminar película existente")
        print("Buscar por ID\n")
        busqueda = input("Ingrese el ID de la pelicula: ")
        while not busqueda.isnumeric():
            busqueda = input("¡ID No válido, debe ser un número!\nIngrese el ID de la película: ")
        for pelicula in range(0, len(lista_peliculas)):
            if lista_peliculas[pelicula]["id"] == int(busqueda):              
                buscar = False
                global dicc_pelicula
                dicc_pelicula = lista_peliculas[pelicula]
                break
        else:
            confirmar = input("El ID ingresado no existe\n¿Desea buscar otor ID?[S/N]: ")
            while confirmar != "s" and confirmar != "n":
                confirmar = input("¡Opciíon no valida!\n¿Desea buscar otor ID?[S/N]: ")
            if confirmar == "n":
                buscar = False
                continue
            else:
                continue
        if desde_donde == "modificacion":
            modificar_pelicula(pelicula)
        elif desde_donde == "baja":
            eliminar_pelicula(pelicula)


def buscar_titulo(desde_donde):
    indices_coincidentes = []
    while True:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente")
        elif desde_donde == "baja":
            print("Eliminar película existente")
        print("Buscar por Titulo\n")
        busqueda = input("Ingrese el titulo de la película: ")
        while busqueda == "":
            busqueda = input("¡No ingreso nada! Ingrese el titulo de la película: ")
        indices_coincidentes.clear()
        contador_coincidencias = 0
        for pelicula in range(0, len(lista_peliculas)):
            if busqueda.lower() in lista_peliculas[pelicula]["titulo"].lower():
                contador_coincidencias += 1
                indices_coincidentes.append(pelicula)
                print(f"Opción: [{contador_coincidencias}] Pelicula: {lista_peliculas[pelicula]['titulo']}.")
        if contador_coincidencias == 0:
            buscar = input("No se encontraton coincidencias\n¿Desea realizar otra busqueda? [S/N]: ").lower()
            while buscar not in "sn":
                buscar = input("¡Se ingreso una opción no valida! Ingrese \"S\" por SI o \"N\" por no: ").lower()
            if buscar == "n":
                break
            else:
                continue
        elif contador_coincidencias > 0:
            indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N]: ").lower()
            no_continuar = True
            while no_continuar: 
                if indice.isalpha() and indice not in "sn":
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N]: ").lower()
                elif indice.isnumeric() and (int(indice) not in range(1, len(indices_coincidentes))):
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N]: ").lower()
                elif not indice.isalpha() and not indice.isnumeric():
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N]: ").lower()
                else:
                    no_continuar = False  
            
            if indice == "s":
                continue
            elif indice == "n":
                break
            else:    
                if desde_donde == "modificacion":
                    modificar_pelicula(indices_coincidentes[int(indice) - 1])
                    break
                elif desde_donde == "baja":
                    eliminar_pelicula(indices_coincidentes[int(indice) - 1])
                    break


def eliminar_pelicula(indice):
    limpiar_pantalla()
    print("CINEMA+\nEliminar película existente\n")
    mostrar_pelicula("eliminar")
    confirmar = ""
    while confirmar != "s" and confirmar != "n":
        confirmar = input("¡Confirma que desea eliminar la película? [S/N]:  ")
    if confirmar == "s":
        peliculas_eliminadas.append(lista_peliculas[indice])
        lista_peliculas.pop(indice)
        guardar()


def histograma():
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
    porsentaje_disponibles = (disponibles / total_peliculas) * 10
    porsentaje_no_disponibles = (no_disponibles / total_peliculas) * 10
    print("Disponibles".ljust(14) + "|" + ("*" * int(porsentaje_disponibles)).ljust(11) + "|" + str(porsentaje_disponibles * 10) + "%")
    print("No Disponibles" + "|" + ("*" * int(porsentaje_no_disponibles)).ljust(11) + "|" + str(porsentaje_no_disponibles * 10) + "%")
    system("pause")

def alta_pelicula():
    agregar = True
    while agregar:
        dicc_pelicula.clear()
        dicc_pelicula["id"] = agregar_id()
        dicc_pelicula["titulo"] = agregar_valor_str("titulo", "alta")
        dicc_pelicula["genero"] = agregar_generos("alta")
        dicc_pelicula["duracion"] = agregar_duracion("alta")
        dicc_pelicula["sinopsis"] = agregar_valor_str("sinopsis", "alta")
        dicc_pelicula["pais"] = agregar_valor_str("pais de origen", "alta")
        dicc_pelicula["idioma"] = agregar_valor_str("idioma", "alta")
        dicc_pelicula["clasificacion"] =  agregar_clasificacion("alta")
        dicc_pelicula["calificacion"] = None
        dicc_pelicula["disponible"] = pelicula_disponible("alta")
        mostrar_pelicula("alta")
        while True:
            guardar_alta = input("¿Agregar pelicula? [S/N]: ")
            if guardar_alta.lower() == "s":
                lista_peliculas.append(dicc_pelicula)
                guardar()
                break
            elif guardar_alta.lower() == "n":
                break
            else:
                print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")
        while True:
            agregar_otra = input("¿Desea agregar otra película? [S/N]: ")
            if agregar_otra.lower() == "n":
                agregar = False
            elif agregar_otra.lower() == "s":
                break
            else:
                print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")

def agregar_id():
    global max_id
    max_id += 1
    return max_id

def agregar_valor_str(clave, desde_donde):# titulo, sinopsis, pais e idioma
    mostrar_pelicula(desde_donde)
    while True:
        valor = input(f"Ingrese el {clave} de la pelicula: ")
        if valor == "":
            print(f"¡El \"{clave.capitalize()}\" no puede estar vacío!")
            continue
        else:
            break
    return valor


def agregar_generos(desde_donde):
    genero.clear()
    agregar_genero = True
    while agregar_genero:
        mostrar_pelicula(desde_donde)
        print("Opciones de genero:")
        mostrar_opciones(generos)
        generos_agregados()
        while True:
            nuevo_genero = input("Seleccione un [Genero]: ")
            if not nuevo_genero.isnumeric():
                print(f"¡Opción ingresada no válida! Debe ingresar un número del 1 al {len(generos)}")
            elif int(nuevo_genero) not in range(1, len(generos)-1):
                print(f"¡Opción ingresada no válida! Debe ingresar un número del 1 al {len(generos)}")
            else:
                break
        if generos[int(nuevo_genero) - 1] not in genero:
            genero.append(generos[int(nuevo_genero )- 1])
        else:
            print("El genero ya esta agreado")
            continue
        generos_agregados()
        otro_genero = input("¿Desea agregar otro genero? [S/N]: ")
        while otro_genero != "s" and otro_genero != "n":
            print("¡Opcion no válida!")
            otro_genero = input("¿Desea agregar otro genero? [S/N]: ")
        if otro_genero.lower() == "n":
            break
    return genero

def generos_agregados():
    if len(genero) > 1:
        print(f"Los generos ya agregados a las pelicula son: {genero}")
    elif len(genero) == 1:
        print(f"Yá agrego un genero a la película: {genero}")
   
def mostrar_opciones(opciones_a_mostrar):
    for x in range(0, len(opciones_a_mostrar)):
        print(f"[{x + 1}] - {opciones_a_mostrar[x]}" )

def agregar_duracion(desde_donde):
    mostrar_pelicula(desde_donde)
    duracion = input("Ingrese la duración de la película en minutos: ")
    while not duracion.isnumeric():
        duracion = input("¡Opción ingresada no válida! El valor ingresado debe ser un número: ")
    return int(duracion)

def agregar_clasificacion(desde_donde):
    mostrar_pelicula(desde_donde)
    mostrar_opciones(clasificacion)
    while True:
        opcion = input("Seleccione una opción para la clasificacion: ")
        if not opcion.isnumeric():
            print(f"!Opción ingresada no válida! Debe ingresar un número del 1 al {len(clasificacion)}")
        elif int(opcion) not in range(1, len(clasificacion)):
            print(f"!Opción ingresada no válida! Debe ingresar un número del 1 al {len(clasificacion)}")
        else:
            break
    return clasificacion[int(opcion) - 1]

def pelicula_disponible(desde_donde):
    mostrar_pelicula(desde_donde)
    disponibilidad_pelicula = input("Está la película disponible en la plataforma? [S/N]: ")
    while disponibilidad_pelicula not in ("s", "n"):
        print("¡Opción ingresada no válida!")
        disponibilidad_pelicula = input("Está la película disponible en la plataforma? [S/N]: ")
    if disponibilidad_pelicula.lower() == "s":
        return True
    else:
        return False

def modificar_pelicula(id): #TODO: hacer la funcion, ver que quede bonita xD
    limpiar_pantalla()
    print("CINEMA+")
    print(f"Aca se modifican la pelicula {id}")
    system("pause")

def listado_peliculas(como):
    limpiar_pantalla()
    print("CINEMA+\n")
    if como == "por titulo":
        print("Listado de películas\n")
        orden_alfabetico = sorted(lista_peliculas, key=lambda pelicula: pelicula["titulo"].lower())
        for pelicula in orden_alfabetico:
            print(f"Titulo      : {pelicula['titulo']},\nGenero      :{pelicula['genero']},\nCalificación:{pelicula['calificacion']}\n")
    elif como == "mayor puntaje":
        print("Las 15 peliculas mejor puntuadas\n")
        orden_calificacion = sorted(lista_peliculas, key=lambda pelicula: pelicula["calificacion"], reverse=True)
        for pelicula in range(1, 16):
            print(f"{str(pelicula).rjust(2)} - Titulo: {orden_calificacion[pelicula]['titulo']}")
            print(f"     Genero: {orden_calificacion[pelicula]['genero']}")
            print(f"     Calificación: {orden_calificacion[pelicula]['calificacion']}")
    #TODO: hacer una opcion para que se pueda ver el listado y volver que no sea pausando la pantalla
    system("pause")

def mostrar_pelicula(desde_donde):
    limpiar_pantalla()
    if desde_donde == "alta":
        print("\nCINEMA+\nAlta de película\n\nPelicula:")
    elif desde_donde == "eliminar":
        print("\nCINEMA+\nBaja de película(Eliminar)\n\nPelicula:")
    elif desde_donde == "modificacion":
        print("CINEMA+\nModificar película existente\n\n\"¡Pelicula modificada!\"\n")
    elif desde_donde == "calificacion":
        print("CINEMA+\nCalificacion de titulos\n")
    for x, y in dicc_pelicula.items():
        print(x.ljust(13) + ": " + str(y))

menu_principal()