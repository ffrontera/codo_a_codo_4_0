import os

peliculas = []
generos = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")
genero = []
clasificacion = ("ATP", "PG", "PG-13", "R", "NC-17") 
# menu principal
opcion = ""
while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
    os.system("cls")
    opcion = input("\n CINEMA+\n\n 1. ABM de películas\n 2. Calificación de títulos\n 3. Reportes y estadísticas\n 4. Salir\n > ")

    # Menu AMB        
    if opcion == "1": 
        opcABM = ""
        while opcABM != "1" and opcABM != "2" and opcABM != "3" and opcABM != "4":
            os.system("cls")
            opcABM = input("\n CINEMA+\n Alta, Baja y modificación de películas\n\n 1. Alta de nueva película\n 2. Modificación de película existente\n 3. Baja de película (eliminar)\n 4. Volver\n >")
            if opcABM == "1": # Alta nueva película
                addOtra = "s"
                while addOtra == "s":
                    os.system("cls")
                    print("\n CINEMA+\n\n")
                    pelicula = {"ID": "", "titulo": "", "genero": [], "duracion": "", "sinopsis": "", "pais": "", "idioma": "", "clasificacion": "", "calificacion": 0.0, "disponible": ""}
                    # ID
                    if len(peliculas) == 0:
                        pelicula["ID"] = 1
                    else:
                        ultimo_id = peliculas[len(peliculas) - 1]["ID"]
                        pelicula["ID"] = ultimo_id + 1
                    while pelicula["titulo"] == "":
                        pelicula["titulo"] = input(" Ingrese el titulo de la pelicula > ")
                    #Cargar generos(list)
                    continuar_genero = True
                    while continuar_genero:
                        opc_genero = input(" Seleccione un genero, si desea ingresar más de uno se le preguntará mas adelante\n [1] Acción\n [2] Animación\n [3] Comedia\n [4] Drama\n [5] Ciencia ficción\n [6] Terror\n [7] Suspenso\n [8] Romántica\n > ")
                        if opc_genero == "1":
                            genero.append(generos[0])
                        elif opc_genero == "2":
                            genero.append(generos[1])
                        elif opc_genero == "3":
                            genero.append(generos[2])
                        elif opc_genero == "4":
                            genero.append(generos[3])
                        elif opc_genero == "5":
                            genero.append(generos[4])
                        elif opc_genero == "6":
                            genero.append(generos[5])
                        elif opc_genero == "7":
                            genero.append(generos[6])
                        elif opc_genero == "8":
                            genero.append(generos[7])
                        else:
                            print(" ¡Seleccionó una opcion incorrecta!")
                        otro_genero = ""
                        while otro_genero != "s" and otro_genero != "n":
                            otro_genero = input(" Desea ingresar otro genero? [S/N] > ").lower()
                            if otro_genero == "n":
                                continuar_genero = False
                    pelicula["genero"] = genero
                    #duracion (int)
                    duracion = ""
                    while not duracion.isnumeric():
                        duracion = input("Ingrese la duración en minutos de la película(En números) > ")
                    else:
                        pelicula["duracion"] = int(duracion)
                    #Sinopsis (string)
                    while pelicula["sinopsis"] == "":
                        pelicula["sinopsis"] = input(" Ingrese una sinópsis de la pelicula > ")
                    #Pais de origen (string)
                    while pelicula["pais"] == "":
                        pelicula["pais"] = input(" Pais de origen de la película > ")
                    #Clasificacion (string)
                    while pelicula["clasificacion"] == "":
                        opc_clasificacion = input(" Elija la clasificacion de la pelicula:\n [1]ATP\n [2]PG\n [3]PG-13\n [4]R\n [5]NC-17\n > ")
                        if opc_clasificacion == "1":
                            pelicula["clasificacion"] = clasificacion[0]
                        elif opc_clasificacion == "2":
                            pelicula["clasificacion"] = clasificacion[1]
                        elif opc_clasificacion == "3":
                            pelicula["clasificacion"] = clasificacion[2]
                        elif opc_clasificacion == "4":
                            pelicula["clasificacion"] = clasificacion[3]
                        elif opc_clasificacion == "5":
                            pelicula["clasificacion"] = clasificacion[4]
                        else:
                            print(" ¡Seleccionó una opcion incorrecta!")              
                    #calificacion (float) - no se ingresa en la carga, es 0 por defecto
                    #Disponible (bool)
                    while pelicula["disponible"] == "":
                        disponibilidad = (input(" Pelicula disponible [S/N] >")).lower()
                        if disponibilidad == "s":
                            pelicula["disponible"] = True
                        elif disponibilidad == "n":
                            pelicula["disponible"] = False
                    peliculas.append(pelicula)
                    addOtra = ""
                    while addOtra != "n" and addOtra != "s":
                        os.system("cls")
                        addOtra = input("\n CINEMA+\n\n ¿Desea ingresar otra película? [S/N]\n >").lower()
            elif opcABM == "2": #Modificacion de pelicula
                opcModificar = ""
                while opcModificar != "1" and opcModificar != "2" and opcModificar != "3":
                    os.system("cls")
                    opcModificar = input("\n CINEMA+\n Modificar película existente\n\n 1. Buscar por ID\n 2. Buscar por titulo\n 3. Volver\n >")
                    if opcModificar == "1":
                        opcModificar = "" #buscar por id
                    elif opcModificar == "2":
                        opcModificar = "" #Buscar por título
                    elif opcModificar == "3": #Volver
                        continue
                    else:
                        os.system("cls")
                        print("\n CINEMA+\n ¡Seleccionó una opcion incorrecta!")
                        os.system("pause")
            elif opcABM == "3": #eliminar pelicula
                opcEliminar = ""
                while opcEliminar != "1" and opcEliminar != "2" and opcEliminar != "3":
                    os.system("cls")
                    opcEliminar = input("\n CINEMA+\n Eliminar una película existente\n\n 1. Buscar por ID\n 2. Buscar por titulo\n 3. Volver\n >")
                    if opcEliminar == "1":
                        opcEliminar = "" #buscar por id
                    elif opcEliminar == "2":
                        opcEliminar = "" #Buscar por título
                    elif opcEliminar == "3": #Volver
                        continue
                    else:
                        os.system("cls")
                        print("\n CINEMA+\n ¡Seleccionó una opcion incorrecta!")
                        os.system("pause")
            elif opcABM == "4": #Volver
                continue
            else:
                os.system("cls")
                print("\n CINEMA+\n ¡Seleccionó una opcion incorrecta!")
                os.system("pause")
            opcABM = ""
        else:
            opcion = ""
    # menu calificacion de titulos
    elif opcion == "2":
        opcion = ""
    
    # menu de reportes
    elif opcion == "3": 
        opcReportes = ""
        while opcReportes != "1" and opcReportes != "2" and opcReportes != "3" and opcReportes != "4":
            os.system("cls")
            opcReportes = input("\n CINEMA+\n Reportes y estadísticas\n\n 1. Listado de películas\n 2. Películas de mayor puntaje\n 3. Porcentaje de películas disponibles en la plataforma\n 4. Volver\n >")
            if opcReportes == "1": #Listado de peliculas
                opcReportes = ""
            elif opcReportes == "2": #Peliculas de mayor puntaje
                opcReportes = ""
            elif opcReportes == "3": #porcentaje de disponibilidad
                opcReportes = ""
            elif opcReportes == "4":
                continue
            else:
                os.system("cls")
                print("\n CINEMA+\n ¡Seleccionó una opcion incorrecta!")
                os.system("pause")
        else:
            opcion = ""

    # Salir        
    elif opcion == "4": 
        os.system("cls")
        salir = ""
        while salir != "s" and salir != "n":
            salir = input("\n CINEMA+\n\n Desea salir del programa [S/N]\n > ").lower()
        if salir == "s":
            os.system("exit")
            os.system("cls")
        else:
            opcion = ""
    else:
        os.system("cls")
        print("\n CINEMA+\n ¡Seleccionó una opcion incorrecta!")
        os.system("pause")