continuar = True
notasIngresadas = 0
sumatoriaNotas = 0
while continuar:
    nota = int(input("Ingrese una nota: "))
    if nota >= 0 and nota <= 10:
        sumatoriaNotas += nota
        notasIngresadas += 1
    else:
        continuar = False


if notasIngresadas == 0:
    print("No se ingresaron notas.")
else:
    promedio = round(sumatoriaNotas / notasIngresadas)
    print(f"El promedio de las notas es de {promedio}")
