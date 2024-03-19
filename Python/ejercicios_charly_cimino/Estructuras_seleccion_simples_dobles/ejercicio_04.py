r = int(input("Ingrese el valor del radio del circulo de centro (0,0): "))
print("Vamos a corroborar si un punto dado (x,y) esta dentro de la circulo.")
x = int(input("Ingrese el valor x del punto: "))
y = int(input("Ingrese le valor y del punto: "))
from math import atan, cos
angulo = atan(y / x)
h = x / cos(angulo)
if h <= r:
    print(f"El punto ({x},{y}) pertenece al circulo.")
else:
    print(f"El punto ({x},{y}) NO pertenece al circulo.")