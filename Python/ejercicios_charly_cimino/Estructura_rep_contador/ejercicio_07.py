print("Vamos a calcular el factorial de un número")
n = int(input("Ingrese el número que desea conocer su factorial (n!): "))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i += 1
    
print(f"{n}! = {factorial}")
