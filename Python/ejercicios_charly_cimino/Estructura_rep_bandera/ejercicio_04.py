continuar = True
contador = 0
a = 0
b = 0
while continuar:
    c = int(input("Ingrese un número entero: "))
    contador += 1
    
    if a - b == b - c:
        continuar = False
    
    a = b
    b = c

print(f"Se ingresaron {contador} números.")