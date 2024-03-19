continuar = True
vocales = 0

while continuar:
    x = input("Ingrese un carácter: ")
    m = x.upper()
    if m == "A" or  m == "E"or  m == "I" or m == "O" or m == "U":
        vocales += 1
    c = input("Desea ingresar otro carácter?[S/N] ")
    if c.upper() == "N":
        continuar = False

print(f"Se ingresaron {vocales} vocales.")    