a = []
b = []
for i in range(0, 5):
    a.append(int(input("Ingrese un número para el arreglo A: ")))
for i in range(0, 5):
    b.append(int(input("Ingrese un número para el arreglo B: ")))

c = []
for x in a:
    for i in b:
        if x == i:
            c.append(x)

print(c)