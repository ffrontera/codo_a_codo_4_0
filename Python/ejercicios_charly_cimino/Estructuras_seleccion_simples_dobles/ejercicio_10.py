numero = input("Ingrese un número de dos, tres o cuatro dígitos:")
digitos = len(numero)
if digitos == 2 and numero[0] == numero[1]:
    print(f"El numero {numero} es capicúa.")
elif digitos == 3 and numero[0] == numero[2]:
    print(f"El numero {numero} es capicúa.")
elif digitos == 4 and numero[0] == numero[3] and numero[1] == numero[2]:
    print(f"El numero {numero} es capicúa.")
else:
    print(f"El numero {numero} NO es capicúa.")