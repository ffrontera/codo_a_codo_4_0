nombres = []
contador = 1
while contador <= 5:
    nombres.append(input("Escriba un nombre: "))
    contador += 1

nombres.sort()

for nombre in nombres:
    print(nombre.capitalize())