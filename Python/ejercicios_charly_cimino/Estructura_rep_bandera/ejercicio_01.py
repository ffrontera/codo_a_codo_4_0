continuar = True
numeros = []
i = 0
while continuar:
    valor = int(input("Ingrese un número, para salir digite el 0: "))
    if valor == 0:
        continuar = False
    else:
       numeros.append(valor)
       i += 1

numeros.sort()

print(f"El mayor número ingresado fue: {numeros[len(numeros) - 1]}.")
print(f"El menor número ingresado fue: {numeros[0]}.")


