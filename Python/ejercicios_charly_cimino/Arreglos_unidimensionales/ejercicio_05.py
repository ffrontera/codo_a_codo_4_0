tiempos = []
for i in range(1, 8):
    tiempo = int(input("Ingrese el tiempo de vuelta: "))
    if i == 1:
        tiempos.append(tiempo)
    elif tiempo > anterior:
        vuelta = "M " + str(tiempo)
        tiempos.append(vuelta)
    elif tiempo < anterior:
        vuelta = "P " + str(tiempo)
        tiempos.append(vuelta)
    anterior = tiempo
print(f"Tiempos de vueltas: {tiempos}")