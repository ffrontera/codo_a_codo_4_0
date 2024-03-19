edad = int(input("Ingrese su edad: "))
genero = input("Indique su genero (\"h\" para hombre, \"f\" para mujer): ")
edadM = 60
edadH = 65
if edad >= edadM and genero == "f" or genero == "F":
    print("¡La femenina esta en edad de jubilarse!")
elif edad >= edadH and genero == "h" or genero == "H":
    print("¡El masculino esta en edad de jubilarse!")
else:
    print("La persona no esta en edad de jubilarse.")
