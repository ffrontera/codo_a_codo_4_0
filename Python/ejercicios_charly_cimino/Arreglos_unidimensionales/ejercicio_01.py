lista = []
continuar = True

while continuar:
    lista.append(int(input("Ingrese un número entero: ")))
    seguir = input("Desea agregar otro número?[S/N]").lower()
    if seguir == "n":
        continuar = False

print("Los Valores de la lista al cuadrado son:")
for x in lista:
    print(x**2)