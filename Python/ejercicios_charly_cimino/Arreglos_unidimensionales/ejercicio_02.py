lista = []
continuar = True

while continuar:
    lista.append(int(input("Ingrese un número entero: ")))
    seguir = input("Desea agregar otro número?[S/N]").lower()
    if seguir == "n":
        continuar = False

lista.reverse()
for x in lista:
    print(1/x)