n = int(input("Ingrese un número: "))
i = 1
sumatoria = 0
while i <= n:
    sumatoria = sumatoria + i**2
    i += 1

print(f"La sumatoria de los cuadrados de los primeros {n} naturales es: {sumatoria}")