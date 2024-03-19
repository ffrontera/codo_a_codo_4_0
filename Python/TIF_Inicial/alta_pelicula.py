from os import system

lista_peliculas = []
pelicula = {}
generos = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")
clasificacion = ("ATP", "PG", "PG-13", "R", "NC-17")
id_max = 0

def limpiar_pantalla(desde_donde):
    system("cls")
    print("CINEMA+")
    if desde_donde == "principal":
        print("\n")
    elif desde_donde == "abm":
        print("Alta, Baja y Modificación de películas")
    elif desde_donde == "alta":
        print("Alta de película")
    elif desde_donde == "modificar":
        print("Modificar película existente")
    elif desde_donde == "baja":
        print("Eliminar una película existente")
    elif desde_donde == "reportes":
        print("Reportes y estadísticas")

def alta_pelicula():
    pelicula.clear()
    pelicula["id"] = pelicula_id() 
    pelicula["titulo"] = pelicula_valor_str("titulo", "alta") 
    pelicula["genero"] = pelicula_generos("alta")
    pelicula["duracion"] = pelicula_duracion("alta")
    pelicula["sinopsis"] = pelicula_valor_str("sinopsis", "alta") 
    pelicula["pais"] = pelicula_valor_str("pais de origen", "alta")
    pelicula["idioma"] = pelicula_valor_str("idioma", "alta") 
    pelicula["clasificacion"] =  pelicula_clasificacion("alta")
    pelicula["calificacion"] = None
    pelicula["disponible"] = pelicula_disponible("alta")
    lista_peliculas.append(pelicula)
    global id_max
    id_max = pelicula["id"]

def pelicula_id():
    global id_max
    id = id_max + 1
    return id

def pelicula_valor_str(clave, desde_donde):# titulo, sinopsis, pais de origen y duracion
    mostrar_pelicula(desde_donde)
    if clave == "sinopsis":
        articulo = "la"
    else:
        articulo = "el"
    valor = input(f"Ingrese {articulo} {clave} de la película: ")
    while valor == "":
        valor = input(f"¡\"{clave.capitalize()}\" no puede estar vacío!\nIngrese {articulo} {clave}: ")
    return valor

def pelicula_generos(desde_donde):
    mostrar_pelicula(desde_donde)
    genero = []
    sumar_genero = True
    while sumar_genero:
        #TODO hacer funcion para mostrar los generos
        opc_genero = input("Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante\n [0] Acción\n [2] Animación\n [2] Comedia\n [3] Drama\n [4] Ciencia ficción\n [5] Terror\n [6] Suspenso\n [7] Romántica\n > ")
        while opc_genero not in ("1","2","3","4","5","6","7","0"):
            mostrar_pelicula(desde_donde)
            print(f"genero       : {genero}")
            print("!Se seleccionó una opción no válida¡")
            opc_genero = input("¡Se ingreso una opcion no válida! Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante:\n [0] Acción\n [1] Animación\n [2] Comedia\n [3] Drama\n [4] Ciencia ficción\n [5] Terror\n [6] Suspenso\n [7] Romántica\n > ")
        if generos[int(opc_genero)-1] not in genero:
            genero.append(generos[int(opc_genero)-1])
        else:
            print(f"¡El genero {generos[int(opc_genero)-1]} ya está agregado!") #TODO: LLevar este aviso arriba con un condicional que lo muestre o no
        otro_genero = ""
        while otro_genero not in ("s", "n"):
            mostrar_pelicula("alta")
            print(f"genero       : {genero}")
            otro_genero = input(" Desea ingresar otro genero? [S/N] > ").lower()
            mostrar_pelicula("alta")
            print(f"genero       : {genero}")
            if otro_genero == "n":
                sumar_genero = False
                return genero
   
def pelicula_duracion(desde_donde):
    mostrar_pelicula(desde_donde)
    duracion = input("Ingrese la duración en minutos de la película: ")
    while not duracion.isnumeric():
        duracion = input("La ¡\"Duración\" debe ser un número!\nIngrese la duración de la película: ")
    return int(duracion) 

def pelicula_clasificacion(desde_donde):
    opcion = input("Elija la clasificacion de la pelicula: ")
    while not opcion.isnumeric() and int(opcion) not in range(0, len(clasificacion) - 1):
        mostrar_pelicula(desde_donde)
        print("!Seleccionó una opción incorrecta!")
        opcion = input("Elija la clasificacion de la pelicula: ")
    return clasificacion[int(opcion) - 1]
    
def pelicula_disponible(desde_donde):
    mostrar_pelicula(desde_donde)
    disponible = input("¡La película está disponible en la plataforma? [S/N]: ").lower()
    while disponible not in ("s", "n"):
        disponible = input("!Opción no válida¡\nDebe ingresar \"S\" si esta disponible o \"N\" si no esta disponible: ")
    if disponible == "s":
        disponible = True
    else:
        disponible = False
    return disponible

def mostrar_pelicula(desde_donde):
    limpiar_pantalla(desde_donde)
    for x, y in pelicula.items():
        print(f"{x.ljust(14)}: {y}")
