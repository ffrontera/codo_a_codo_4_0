numero = int(input("Ingrese un número del 1 al 10: "))
print("-" * 12)
print(f"Tabla del {numero}")
for i in range(0, 11):
    print(f"{i} x {numero} = {i * numero}")