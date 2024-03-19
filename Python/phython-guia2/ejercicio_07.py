max = 0
for i in range(1, 6):
    numero = int(input("Ingrese un número: "))
    if numero > max:
        max = numero
        aparicion = i

print(f"El número más alto ingresado fue el {max} y fue en la posición {aparicion}")