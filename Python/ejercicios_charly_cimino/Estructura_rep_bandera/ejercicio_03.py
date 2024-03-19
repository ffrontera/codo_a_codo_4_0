l = int(input("Ingrese un número del 1-10: "))
sumatoria = 0
n = 1
while sumatoria < l:
    sumatoria = 1/n + sumatoria
    n += 1

print(f"La cantidad de terminos para cumplir la serie armonica es: {n - 1}")