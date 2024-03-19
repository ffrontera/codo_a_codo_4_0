from math import fabs
alumnos = int(input("Ingrese la cantidad de alumnos: "))
sillas = int(input("Ingrese la cantidad de sillas disponibles: "))
sillas_restantes = sillas - alumnos
if sillas_restantes >= 0:
    print("Las sillas son suficientes para todos.")
else:
    print(f"Las sillas NO son suficientes, faltan {int(fabs(sillas_restantes))} sillas.")