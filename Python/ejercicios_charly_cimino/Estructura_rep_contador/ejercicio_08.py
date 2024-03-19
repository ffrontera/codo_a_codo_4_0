print("Vamos a ingresar tres números (A, B y C), \npara mostrar los múltiplos de C comprendidos entre A y B")
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))
i = a + 1
while i <= b - 1:
    if i % c == 0:
        print(i)
    i += 1