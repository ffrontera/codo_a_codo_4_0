x = int(input("Ingrese un número del 0 al 10: "))
i = 0
print(f"La tabla del {x} es:")
while i <= 10:
    print(f"{x} X {i} =", (x * i))
    i += 1