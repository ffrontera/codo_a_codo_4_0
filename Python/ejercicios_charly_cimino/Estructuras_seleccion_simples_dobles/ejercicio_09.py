a = int(input("Ingrese el lado a del triangulo: "))
b = int(input("Ingrese el lado b del triangulo: "))
c = int(input("Ingrese el lado c del triangulo: "))
if a + b < c or a + c < b or b + c < a: #desigualdad triangular
    print("Los lados ingresados no son de un triangulo valido.")
elif a == b and b == c:
    print(f"El triangulo {a} , {b} , {c} es equilátero.")
elif a != b and b != c and a != a:
    print(f"El triangulo {a} , {b} , {c} es escaleno.")
else:
    print(f"El triangulo {a} , {b} , {c} es isósceles.")