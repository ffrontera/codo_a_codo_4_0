t = int(input("ingrese un número entero:"))
m = int(input("ingrese otro número entero:"))
array = []
for i in range(2, t):
    array.append(m * i)

print(array)