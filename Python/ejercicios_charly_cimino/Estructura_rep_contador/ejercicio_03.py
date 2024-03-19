n = int(input("Ingrese la cantidad de terminos a usar en la formila de Leibniz para Pi: "))
sumatoria = 0
i = 0
while i <= n -1:
    sumatoria = pow(-1, i)  / ((2 * i) +1) + sumatoria
    i += 1

print(f"El valor de Pi usando {n} terminos en la formula de Leibniz es: {4*sumatoria}")