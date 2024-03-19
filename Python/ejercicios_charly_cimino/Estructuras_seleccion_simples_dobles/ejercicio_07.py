numeros = []
i = 0

while i < 3 :
    numeros.append(input("Ingrese un numero entero: "))
    i += 1

numeros.sort()
i = 0
print("Los numeros ingresados de mayor a menor son: ")
while i < 3:
    print(numeros[i])
    i += 1