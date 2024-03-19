n = int(input("ingrese la cantidad de terminos de la sucecion de fibonacci a conocer: "))
i = 1
f = 0
b = 1
while i <= n:
    print(f)
    a = b
    b = f
    f = a + b
    i += 1
