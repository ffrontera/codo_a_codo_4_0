incorrecto = True
while incorrecto:
    x = int(input("Ingrese un número entero mayor a 1: "))
    if x > 1:
        incorrecto = False

for i in range(2, x-1):
    resto = x % i
    if resto == 0:
        print(f"El número {x} ¡NO es un número primo!.")
        break
else:
    print(f"El número {x} ¡Es un número primo!.")