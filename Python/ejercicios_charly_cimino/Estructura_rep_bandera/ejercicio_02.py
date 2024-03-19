notas = []
continuar = True
i = 0
while continuar:
    nota = int(input("Ingrese una nota: "))
    if nota < 0 or nota > 10:
        continuar = False
    else:
        notas.append(nota)
        i += 1

sumatoria = 0
for x in notas:
    sumatoria = sumatoria + x

promedio = sumatoria / len(notas)

print(f"El promedio de notas es: {promedio}.")