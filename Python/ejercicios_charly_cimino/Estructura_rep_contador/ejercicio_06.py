i = 1
max = 0
while i <= 5:
    x = int(input("Ingrese un número: "))
    if x > max:
        max = x
        orden = i
    i += 1    
print(f"El mayor número ingresado fue {max} y aparicio en el orden {orden}.")
