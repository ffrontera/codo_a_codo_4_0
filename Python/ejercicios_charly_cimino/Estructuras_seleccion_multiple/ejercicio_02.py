lado = input("Ingrese el número obtenido al lanzar el dado[1-6]: ")
if lado == "1":
    print("El número de la cara opuesta es 6.")
elif lado == "2":
    print("El número de la cara opuesta es 5.")
elif lado == "3":
    print("El número de la cara opuesta es 4.")
elif lado == "4":
    print("El número de la cara opuesta es 3.")
elif lado == "5":
    print("El número de la cara opuesta es 2.")
elif lado == "6":
    print("El número de la cara opuesta es 1.")
else:
    print("El número ingresado no corresponde a una cara del dado[1-6].")