b = int(input("Ingrese un número \"b\": "))
e = int(input("Ingrese el número a elevar el numero b: "))
i = 0
a = 1
while i < e:
    a = a * b
    i += 1

print(f"El numero {b} elevado a la {e} da como resultado {a}")