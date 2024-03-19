from os import system
from json import load, dump
from random import randint

def limpiar_pantalla():
    system("cls")

with open("peliculas.json") as archivo:
    peliculas = load(archivo)

lista_peliculas = peliculas["peliculas"]
peliculas_eliminadas = peliculas["peliculas eliminadas"]
max_id = peliculas["max_id"]
dicc_pelicula = {}
genero = []
clasificacion = ("ATP", "PG", "PG-13", "R", "NC-17")
generos = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")
indices_coincidentes = []

def guardar():
    peliculas["peliculas"] = lista_peliculas
    peliculas["max_id"] = max_id
    peliculas["peliculas eliminadas"] = peliculas_eliminadas
    with open("peliculas.json", "w") as archivo_peliculas:
        dump(peliculas, archivo_peliculas, indent=4)

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

def menu_principal():
    salir = False
    while not salir:
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
                print("CINEMA+\n¡Gracias por ser parte de nuestro staff!")
                salir = True

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
            while not calificacion.isnumeric:
                calificacion = input("¡Calificacion no válida! Ingrese un número del 1 al 10 para calificar la película > ")
            if dicc_pelicula["calificacion"] == 0.0:
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
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-3]\n> ")
        if opcion == "1":
            buscar_id(desde_donde) 
        elif opcion == "2":
            buscar_titulo(desde_donde)
        elif opcion == "3":
           break 

def alta_pelicula():
    agregar = True
    while agregar:
        limpiar_pantalla()
        global max_id
        dicc_pelicula.clear()
        print("CINEMA+")
        print("Alta de nueva película\n")
        if max_id == None:
            dicc_pelicula["id"] = 1
        else:     
            dicc_pelicula["id"] = max_id + 1
        mostrar_pelicula("alta")
        dicc_pelicula['titulo'] = input("Ingrese el titulo de la pelicula > ")
        while dicc_pelicula['titulo'] == "":
            limpiar_pantalla()
            mostrar_pelicula("alta")
            dicc_pelicula['titulo'] = input("¡Debe ingresar un título! Ingrese el titulo de la pelicula > ")
        sumar_genero = True
        genero.clear()
        mostrar_pelicula("alta")
        while sumar_genero:
            opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
            while opc_genero not in "12345678" or opc_genero == "":
                mostrar_pelicula("alta")
                print(f"genero       : {genero}")
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
                print(f"¡El genero {generos[int(opc_genero) -1]} ya está agregado!")
            otro_genero = ""
            while otro_genero != "s" and otro_genero != "n":
                mostrar_pelicula("alta")
                print(f"genero       : {genero}")
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
        dicc_pelicula["sinopsis"] = input("Ingrese una sinópsis de la pelicula > ")
        while dicc_pelicula["sinopsis"] == "":
            dicc_pelicula["sinopsis"] = input("El campo no puede estar vacío\nIngrese una sinópsis de la pelicula > ")
        mostrar_pelicula("alta")
        dicc_pelicula["pais"] = input("Ingrese el país de origen de la pelicula > ")
        while dicc_pelicula["pais"] =="":
            dicc_pelicula["pais"] = input("El campo no puede quedar vácio\nIngrese el país de origen de la pelicula > ")
        mostrar_pelicula("alta")
        dicc_pelicula["idioma"] = input("Ingrese el idioma de la pelicula > ")
        while dicc_pelicula["idioma"] == "":
            mostrar_pelicula("alta")
            dicc_pelicula["idioma"] = input("¡El campo idioma no puede quedar vacío!\nIngrese el idioma de la pelicula > ")
        mostrar_pelicula("alta")
        opciones_clasificar = [1,2,3,4,5]
        opcion_clasificacion = input("Elija la clasificacion de la pelicula:\n [1]ATP\n [2]PG\n [3]PG-13\n [4]R\n [5]NC-17\n > ")
        while  opcion_clasificacion == "" and opcion_clasificacion not in opciones_clasificar:
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
        confirmar = input("¿Confirma que quiere agregar la pelicula?[S/N] > ").lower()
        while confirmar not in "sn":
            confirmar = input("¡Opción incorrecta!\n¿Confirma que quiere agregar la pelicula?[S/N] > ").lower()
        if confirmar == "s":
            lista_peliculas.append(dicc_pelicula)
            if max_id == None:
                max_id = 1
            else:
                max_id += 1
            guardar()
            print(f"La pelicula: \"{dicc_pelicula['titulo']}\" ¡Se dio de alta con éxito!")
        agregar_otra = input("¿Desea agregar otra pelicula? [S/N]\n> ").lower()
        while agregar_otra != "s" and agregar_otra != "n":
            agregar_otra = input("¡Se seleccionó una opcion no válida!\n¿Desea agregar otra pelicula? [S/N]\n> ")
        if agregar_otra == "n":
            agregar = False

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
        busqueda = input("Ingrese el ID de la pelicula > ")
        while not busqueda.isnumeric():
            busqueda = input("¡ID No válido, debe ser un número!\nIngrese el ID de la película > ")
        for pelicula in range(0, len(lista_peliculas)):
            if lista_peliculas[pelicula]["id"] == int(busqueda):              
                buscar = False
                global dicc_pelicula
                dicc_pelicula = lista_peliculas[pelicula]
                break
        else:
            confirmar = input("El ID ingresado no existe\n¿Desea buscar otor ID?[S/N]:\n>")
            while confirmar != "s" and confirmar != "n":
                confirmar = input("¡Opciíon no valida!\n¿Desea buscar otor ID?[S/N]:\n>")
            if confirmar == "n":
                buscar = False
                continue
            else:
                continue
        if desde_donde == "modificacion":
            modificacion(pelicula)
        elif desde_donde == "baja":
            eliminar(pelicula)


def buscar_titulo(desde_donde):
    while True:
        limpiar_pantalla()
        print("CINEMA+")
        if desde_donde == "modificacion":
            print("Modificar película existente")
        elif desde_donde == "baja":
            print("Eliminar película existente")
        print("Buscar por Titulo\n")
        busqueda = input("Ingrese el titulo de la película > ")
        while busqueda == "":
            busqueda = input("¡No ingreso nada! Ingrese el titulo de la película > ")
        indices_coincidentes.clear()
        contador_coincidencias = 0
        for pelicula in range(0, len(lista_peliculas)):
            if busqueda.lower() in lista_peliculas[pelicula]["titulo"].lower():
                contador_coincidencias += 1
                indices_coincidentes.append(pelicula)
                print(f"Opción: [{pelicula}] Pelicula: {lista_peliculas[pelicula]['titulo']}.")
        if contador_coincidencias == 0:
            buscar = input("No se encontraton coincidencias\n¿Desea realizar otra busqueda? [S/N] > ").lower()
            while buscar not in "sn":
                buscar = input("¡Se ingreso una opción no valida! Ingrese \"S\" por SI o \"N\" por no > ").lower()
            if buscar == "n":
                break
            else:
                continue
        elif contador_coincidencias > 0:
            indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N] > ").lower()
            no_continuar = True
            while no_continuar: 
                if indice.isalpha() and indice not in "sn":
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N] > ").lower()
                elif indice.isnumeric() and (int(indice) not in indices_coincidentes):
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N] > ").lower()
                elif not indice.isalpha() and not indice.isnumeric():
                    print("¡Opcion no válida!")
                    indice = input("Si encontro la pelicula, ingrese la opción correspondiente,\npara realizar otra busqueda ingrese [S], para volver al menu anterior ingrese [N] > ").lower()
                else:
                    no_continuar = False  
            
            if indice == "s":
                continue
            elif indice == "n":
                break
            else:    
                if desde_donde == "modificacion":
                    modificacion(int(indice))
                    break
                elif desde_donde == "baja":
                    eliminar(int(indice))
                    break
        
def modificacion(indice):
    limpiar_pantalla()
    print("CINEMA+\nModificar película existente\n")
    for x, y in lista_peliculas[indice].items():
        print(x.ljust(14), y)
        if x == "id":
            dicc_pelicula[x] = y
            continue
        elif x == "calificacion":
            dicc_pelicula[x] = y
            continue
        modificar = input(f"¿Desea modificar {x}? [S/N]\n> ").lower()
        while modificar != "s" and modificar != "n":
            modificar = input(f"¡Se seleccionó una opcion no válida!\n¿Desea modificar {x}? [S/N]\n> ")
        if modificar == "s":
            if x == "genero":
                genero.clear()
                sumar_genero = True
                while sumar_genero:
                    opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
                    while opc_genero == "" or opc_genero not in "12345678" :
                        mostrar_pelicula("modificacion")
                        print(f"genero       : {genero}")
                        print("!Se seleccionó una opción no válida¡")
                        opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante:\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
                    if generos[int(opc_genero) - 1] not in genero:
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
                    otro_genero = ""
                    while otro_genero != "s" and otro_genero != "n":
                        otro_genero = input(" Desea ingresar otro genero? [S/N] > ").lower()
                        mostrar_pelicula("modificacion")
                        print(f"genero       : {genero}")
                        if otro_genero == "n":
                            sumar_genero = False
                            dicc_pelicula["genero"] = genero
            elif x == "clasificacion":
                opcion_clasificacion = input("Elija en nuevo valor para clasificacion de la pelicula:\n [1]ATP\n [2]PG\n [3]PG-13\n [4]R\n [5]NC-17\n > ")
                while opcion_clasificacion  not in "12345":
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
            elif x == "duracion":
                duracion = input("Ingrese la duración en minutos de la película ¡En números! > ")
                while not duracion.isnumeric(): 
                    mostrar_pelicula("modificacion")
                    duracion = input("!Valor no válido¡ Ingrese la duración en minutos de la película ¡En números! > ")
                else:
                    dicc_pelicula["duracion"] = int(duracion)
            elif x == "disponible":
                disponibilidad = input("¿Esta disponible en la plataforma?[S/N] > ").lower()
                while disponibilidad != "s" and disponibilidad != "n":
                    disponibilidad = input("!Opción incorrecta!\n¡¿Esta disponible en la plataforma?[S/N] > ")
                if disponibilidad == "s":
                    dicc_pelicula["disponible"] = True
                else:
                    dicc_pelicula["disponible"] = False
            else:
                dicc_pelicula[x] = input(f"Ingrese en nuevo valor para {x} > ")
                while dicc_pelicula[x] == "":
                    dicc_pelicula[x] = input(f"El campo no puede estar vacío\nIngrese el nuevo valor para {x} > ")
        else:
            dicc_pelicula[x] = y    
    mostrar_pelicula("modificacion")
    print("\n\"¡Pelicula sin modificar!\"\n")
    for x, y in lista_peliculas[indice].items():
        print(x.ljust(13) + ": " + str(y))
    guardar = input("\n¿Desea guardar los cambios?[S/N] > ")
    while guardar not in "sn" and guardar == "":
        guardar = input("¡Opción incorrecta!\n¿Desea guardar los cambios? [S] para guardar, [N] para no guardar > ")
    if guardar == "s":
        lista_peliculas[indice] = dicc_pelicula
        guardar()
        print("!Pelica modificada con éxito!")
        system("pause")    

def eliminar(pelicula): 
    limpiar_pantalla()
    print("CINEMA+\nEliminar película existente\n")
    mostrar_pelicula("eliminar")
    confirmar = ""
    while confirmar != "s" and confirmar != "n":
        confirmar = input("¡Confirma que desea eliminar la película? [S/N] > ")
    if confirmar == "s":
        peliculas_eliminadas.append(lista_peliculas[pelicula])
        lista_peliculas.pop(pelicula)
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

menu_principal()