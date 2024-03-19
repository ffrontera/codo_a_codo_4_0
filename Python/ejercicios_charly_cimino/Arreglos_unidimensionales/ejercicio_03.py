conjunto = set()
continuar = True

while continuar:
    conjunto.add(int(input("Ingrese un número entero: ")))
    seguir = input("Desea agregar otro número?[S/N]").lower()
    if seguir == "n":
        continuar = False
else:
    print(conjunto)