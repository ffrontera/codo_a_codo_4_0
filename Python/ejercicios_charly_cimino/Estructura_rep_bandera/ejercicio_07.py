total = 0
continuar = True
while continuar:
    unitario = float(input("Ingrese el precio unitario del arículo: "))
    cantidad = int(input("Ingrese la cantidad: "))
    total = total + cantidad * unitario
    c = input("¿Desea ingresar otro artículo?[S/N] ").upper()
    if c == "N":
        continuar = False

print(f"El monto de la factura es: ${total}.")