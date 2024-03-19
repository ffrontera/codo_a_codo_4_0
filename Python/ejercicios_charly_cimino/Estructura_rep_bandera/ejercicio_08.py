continuar = True
ingles = 0
frances = 0
portugues = 0
aleman = 0
alumnos = 0
while continuar:
    opcion = input("Ingrese opción: [I]nglés - [F]rancés - [P]ortugués - [A]lemán ").upper()
    if opcion == "I":
        ingles += 1
        alumnos += 1
    elif opcion == "F":
        frances += 1
        alumnos += 1
    elif opcion == "P":
        portugues += 1
        alumnos += 1
    elif opcion == "A":
        aleman +=1
        alumnos += 1
    else:
        print("Opcion no válida")
    c = input("Desea cargar otro alumno? [S/N]: ").upper()
    if c == "N":
        continuar = False

print(f"Inglés fue elegido por {ingles} alumnos ({ingles*100/alumnos}%)")
print(f"Francés fue elegido por {frances} alumnos ({frances*100/alumnos}%)")
print(f"Portugués fue elegido por {portugues} alumnos ({portugues*100/alumnos}%)")
print(f"Alemán fue elegido por {aleman} alumnos ({aleman*100/alumnos}%)")

print("Ingles    " + ("*" * round(ingles*100/alumnos)))
print("Fances    " + ("*" * round(frances*100/alumnos)))
print("Portugues " + ("*" * round(portugues*100/alumnos)))
print("Aleman    " + ("*" * round(aleman*100/alumnos)))