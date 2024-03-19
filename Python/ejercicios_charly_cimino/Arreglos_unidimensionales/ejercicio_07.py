a = []
b = []
c = []
for i in range(0, 5):
    a.append(int(input("Ingrese un número entero para el arreglo a: ")))
for i in range(0, 5):
    b.append(int(input("Ingrese un número entero para el arreglo b: ")))
for i in range(0, 5):
    c.append(a[i] + b[i])

print(a)
print(b)
print(f"A + B = C: {c}")