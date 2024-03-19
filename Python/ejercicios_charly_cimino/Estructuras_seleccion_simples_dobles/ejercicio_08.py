x = int(input("Ingrese un número entero: "))
y = int(input("Ingrese un número entero: "))
if x > y and x % y == 0:
    print(f"El número {x} es divisible por {y}")
elif y > x and y % x == 0:
    print(f"El número {y} es divisible por {x}")
else:
    print("El número mayor ingresado no es divisible por el número menor ingresado.")