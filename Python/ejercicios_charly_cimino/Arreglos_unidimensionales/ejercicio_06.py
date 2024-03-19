numeros = []   
for i in range(1, 200):
    numeros.append(i)

sumatoria = 0
for x in numeros:
    sumatoria += x

print(f"La suma de los valores del arreglo es: {sumatoria}")