from json import load, dump
import os

with open("peliculas.json") as archivo:
    lista_peliculas = load(archivo)
with open("peliculas_eliminadas.json") as archivo:    
    peliculas_eliminadas = load(archivo)
with open("max_id.json") as archivo:
    max_id = load(archivo)

opc_menu_principal = ("ABM películas", "Calificación de títulos", "Reportes y estadistica", "Salir")
opc_menu_abm = ("Alta de nueva película", "Modificación de película existente", "Baja de película (Eliminar)", "Volver")
opc_menu_reporte = ("Listado de películas", "Películas de mayor puntaje", "Porcentaje de películas disponibles en la plataforma", "Volver")
opc_menu_buscar = ("Buscar por ID", "Buscar por título", "Volver")
dicc_pelicula = {}
indices_buscar_pelicula = []
titulos_buscar_pelicula =[]


def limpiar_pantalla():
  os.system('cls' if os.name == 'nt' else 'clear')

def guardar():
   with open("peliculas.json", "w") as archivo_guardar:
     dump(lista_peliculas, archivo_guardar, indent=4)
   with open("max_id.json", "w") as archivo_guardar:
     dump(max_id, archivo_guardar, indent=4)
   with open("peliculas_eliminadas.json", "w") as archivo_guardar:
     dump(peliculas_eliminadas, archivo_guardar, indent=4)

def mostrar_opciones(opciones_a_mostrar):
    for x in range(0, len(opciones_a_mostrar)):
        print(f"[{x + 1}] - {opciones_a_mostrar[x]}" )

def mostrar_pelicula():
    for x, y in dicc_pelicula.items():
        print(x.ljust(13) + ": " + str(y))

def imprimir_menu_principal():
    while True:
        limpiar_pantalla()
        print("CINEMA+\n")
        mostrar_opciones(opc_menu_principal)
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
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
        limpiar_pantalla()
        mostrar_opciones(opc_menu_abm)
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
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
    #TODO: iterar 10 peliculas al azar listando la ficha completa de cada pelicula.
    limpiar_pantalla()
    print("CINEMA+\nCalificacion de titulos\n")
    print("Acá se califican las películas")
    os.system("pause")

def imprimir_menu_reportes():
    while True:
        limpiar_pantalla()
        mostrar_opciones(opc_menu_reporte)
        opcion = input("> ")
        while opcion not in "1234":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-4]\n> ")
        if opcion == "1":
            listar_peliculas("por titulo")
        elif opcion == "2":
            listar_peliculas("mayor puntaje")
        elif opcion == "3":
            mostrar_histograma()
        elif opcion == "4":
            break

def imprimir_menu_buscar():
    while True:
        limpiar_pantalla()
        print("CINEMA+")
        mostrar_opciones(opc_menu_buscar)
        opcion = input("> ")
        while opcion not in "123":
            opcion = input("¡Opción No valida! Ingrese nuevamente una opción[1-3]\n> ")
        if opcion == "1":
           indice = buscar_id() 
           return indice
        elif opcion == "2":
            buscar_titulo()
        elif opcion == "3":
            break

def buscar_id():
   limpiar_pantalla()
   while True:
      print("Buscar por ID\n")
      while True:
          busqueda = input("Ingrese el ID de la pelicula: ")
          if not busqueda.isnumeric():
             print("¡Opcion no valida! Debe ingresar un numero")
          else:
             break
      for pelicula in range(0, len(lista_peliculas)):
         if lista_peliculas[pelicula]["id"] == int(busqueda):
            return pelicula #Retorna el indice de la pelicula en lista_peliculas
      else:
         print("¡El id ingresado no existe!")


def buscar_titulo():
    indices_buscar_pelicula.clear()
    titulos_buscar_pelicula.clear()
    while True:
       limpiar_pantalla()
       print("CINEMA+")
       print("Buscar por Titulo\n")
       busqueda = input("Ingrese el titulo de la película: ")
       while busqueda == "":
          print("¡Debe ingresar un titulo o palabra a buscar!")
          busqueda = input("Ingrese el titulo de la película: ")
       for pelicula in range(0, len(lista_peliculas)):#pelicula es el indice 
          if busqueda in lista_peliculas[pelicula]["titulo"]:  # generamos dos listas una para los indices y la otra para el titulo
             indices_buscar_pelicula.append(pelicula)
             titulos_buscar_pelicula.append(lista_peliculas[pelicula]["titulo"])
       mostrar_opciones(titulos_buscar_pelicula)      
       os.system("pause")
       #TODO: realizar busqueda, condicional si no existe avisar    
       break


def eliminar_pelicula(indice): #TODO: agregar indice como parametro
    limpiar_pantalla()
    print("CINEMA+\nEliminar película existente\n")
    global dicc_pelicula
    dicc_pelicula = lista_peliculas[indice]
    mostrar_pelicula()
    confirmar = ""
    while confirmar != "s" and confirmar != "n":
        confirmar = input(f"¿Confirma que desea eliminar la película {lista_peliculas[indice]['titulo']}? [S/N]: ")
    if confirmar == "s":
       peliculas_eliminadas.append(listar_peliculas[indice])
       lista_peliculas.pop(indice)
       guardar() 
       print("Se elimina la película")
       os.system("pause") 


def mostrar_histograma(): #TODO: crear función real para histograma
    limpiar_pantalla()
    print("CINEMA+\nPorcentaje de películas disponibles en la plataforma\n")
    print("Disponibles".ljust(14) + "|" + "*"*8)
    print("No Disponibles" + "|" + "*"*2)
    os.system("pause")

def cargar_pelicula():
   agregar = True
   while agregar:
      dicc_pelicula.clear()
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
      mostrar_pelicula()
      while True:
         guardar_alta = input("¿Desea agregar la pelicula? [S/N]: ")
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
         if agregar_otra.lower() == "s":
            break
         elif agregar_otra.lower() == "n":
            agregar = False
            break
         else:
            print("¡Opción ingresada no válida! Debe ingresar \"S\" por si o \"N\" por no")

def agregar_id(): 
   global id_max
   id = id_max + 1
   return id

def agregar_valor_str(clave):# titulo, sinopsis, pais e idioma
   valor = ""
   while valor == "":
      valor = input(f"Ingrese el {clave} de la pelicula: ")
   return valor

def agregar_generos():
   lista_generos=["Acción","Animación","Comedia","Drama","Ciencia Ficción","Terror","Suspenso","Romántica"]
   mostrar_opciones(lista_generos)
   generos=[]
   otro ="s"
   while otro.lower() in ("s"):
      opcion_genero = input("> ")
      if not opcion_genero.isnumeric() :
         print("¡Opcion no válida! Debe ingresar un número")
      elif int(opcion_genero) not in range(1, len(lista_generos)):
         print(f"¡Opcion no valida! Debe ingresar un numero 1 al {len(lista_generos)}")
      elif lista_generos[int(opcion_genero) - 1] in generos:
         print("¡El genero ingresado ya esta cargado!")
      else:
         generos.append(lista_generos[int(opcion_genero) - 1])
      otro=input ("Desea ingresar otro género (S/N)?")
      while otro.lower()!="n" and otro.lower()!="s":
          otro=input("Opción inválida, ingrese S/N: ").lower()
      if otro.lower()== "n":
          return generos


def agregar_duracion():#Cristina
    print("Ingrese duración de la película en minutos(1-999)")
    duracion = str(input("> "))
    while duracion<"0" or duracion>"999" or not duracion.isnumeric():
      print ("Ingrese valor entre 0 y 999 minutos")
      duracion = input("> ")  
    else:
      return int(duracion) 



def agregar_clasificacion():
   print ("Listado de clasificaciones disponibles")
   lista_clasificacion=["ATP","PG","PG-13","R","NC-17"]
   mostrar_opciones(lista_clasificacion)
   while True:
      opcion_calificacion=input("Ingrese calificación de la película: ")
      if not opcion_calificacion.isnumeric() :
        print("¡Opcion no válida! Debe ingresar un número")
      else:
        if int(opcion_calificacion) not in range(1, len(lista_clasificacion)):
          print(f"¡Opcion no valida! Debe ingresar un numero 1 al {len(lista_clasificacion)}")
        else:
          return lista_clasificacion[int(opcion_calificacion)-1]

def agregar_disponibilidad():
  disponible=input("Ingrese disponibilidad en streaming (S/N): ").lower()
  while disponible!="s" and disponible!="n":
      disponible= input("Opcion inválida, ingrese (S/N):").lower()
  if disponible=="s": 
      return True
  elif disponible=="n":
      return False 

def modificar_pelicula(id):
    limpiar_pantalla()
    print("CINEMA+")
    print(f"Aca se modifican la pelicula {id}")
    os.system("pause")

def listar_peliculas(como):
    limpiar_pantalla()
    print("CINEMA+")
    if como == "por titulo":
        print("Listado de películas\n")
    elif como == "mayor puntaje":
        print("Las 15 peliculas mejor puntuadas\n")
    print("opcion para volver al menu reportes")
    os.system("pause")



imprimir_menu_principal()