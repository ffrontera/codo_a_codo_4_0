n = int(input("Ingrese un número: "))
mostrados = 1
i = 3
while mostrados <= n:
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        mostrados += 1
    
    i += 1
