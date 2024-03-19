max = 0
for i in range(1, 6):
    numero = int(input("Ingrese un número: "))
    if numero > max:
        max = numero

print(f"El número mas alto ingresado fue el {max}")