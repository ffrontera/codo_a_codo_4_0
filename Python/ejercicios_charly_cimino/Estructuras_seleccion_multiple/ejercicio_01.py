x = int(input("Ingrese un número entero: "))
y = int(input("Ingrese un número entero: "))
operador = input("Ingrese el operador matemático a ejecutar (+ , - , * , /): ")
if operador == "+":
    print(x + y)
elif operador == "-":
    print(x - y)
elif operador == "*":
    print(x * y)
elif operador == "/":
    print(x / y)
else:
    print("El operador ingresado no es valido")