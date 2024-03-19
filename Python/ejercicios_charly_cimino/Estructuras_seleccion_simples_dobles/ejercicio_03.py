a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
cociente= int(a / b)
resto = a % b
print(f"el resultado entero del cociente entero de {a} y {b} es: {cociente}.")
if a % b != 0 :
    print(f"el resto de la division es: {resto}") 