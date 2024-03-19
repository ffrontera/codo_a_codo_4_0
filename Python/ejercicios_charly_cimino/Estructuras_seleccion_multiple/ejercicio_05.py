print("Vamos a ingresar un número y lo convertiremos en número romano")
romanos = {
    "1": "I",
    "5": "V",
    "10": "X",
    "50": "L",
    "100": "C",
    "500": "D",
    "1000": "M"
}
num = input("Ingrese el número a convertir(1,5,10,50,100,500,1000)")
coincidencia = False
for x in romanos:
    if num == x:
        print(f"El {num} en número romano es: {romanos[x]}")
        coincidencia = True
        break

if coincidencia == False:
    print("El numero ingresado no puede ser convertido por este programa =(") 
