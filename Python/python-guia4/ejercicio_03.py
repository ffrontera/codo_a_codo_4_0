notas = [ 8, 6, 7, 2, 8, 9, 3, 4, 6, 10]
sumatoria = 0
aplazos = []
cant_aplazos = 0
for nota in notas:
    sumatoria += nota
    if nota < 4:
        aplazos.append(nota)
        cant_aplazos += 1
promedio = sumatoria / len(notas)
print(f"El promedio de las notas es: {promedio}")

print(f"La cantidad de aplazos es: {cant_aplazos}. Son las siguientes notas:")
for aplazo in aplazos:
    print(aplazo)

notas.sort(reverse=True)
print(f"Las notas fueron: {notas}")