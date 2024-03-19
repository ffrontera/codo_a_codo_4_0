carniceria = []
verduleria = []
almacen = []
continuar_ingresando = True
while continuar_ingresando:
    producto = input("Ingrese producto a comprar: ")
    lista_incorrecta = True
    while lista_incorrecta:
        tienda = input("Agrear a la lista de [C]arnicería - [V]erdulería - [A]lmacen: ").lower()
        if tienda == "c":
                if producto not in carniceria:
                    carniceria.append(producto)
                    lista_incorrecta = False
        elif tienda == "v":
            verduleria.append(producto)
            lista_incorrecta = False
        elif tienda == "a":
            almacen.append(producto)
            lista_incorrecta = False
        else:
            print("Se ingreso una opción no válida")
    opcion_otro = True
    while opcion_otro:
        continuar = input("Desea continuar ingresando productos para comprar? [S/N]: ").lower()
        if continuar == "s" or continuar == "si":
            opcion_otro = False
        elif continuar == "n" or continuar == "no":
            opcion_otro = False
            continuar_ingresando = False
        else:
            print("Opcion no válida.")
else:
    print(f"La lista de la carniceria tiene {len(carniceria)} artículos.")
    if len(carniceria) != 0:    
        for x in carniceria:
            print(x)
    else:
        print("Sin productos.")
    print(f"La lista de la verduleria tiene {len(verduleria)} artículos.")
    if len(verduleria) != 0:
        for x in verduleria:
            print(x)
    else:
        print("Sin productos.")
    print(f"La lista del almacen tiene {len(almacen)} articulos.")
    if len(almacen) != 0:
        for x in almacen:
            print(x)
    else:
        print("Sin productos.")
    articulos_totales = len(carniceria) + len(verduleria) + len(almacen)
    print(f"El total de productos a compras es: {articulos_totales}.")