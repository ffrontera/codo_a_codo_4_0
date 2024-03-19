print("¡Vamos a descubrir tu signo del zodiaco!")
dia = input("Ingrese el dia de su cumpleaños: ")
mes = input("Ingrese el mes de su cumpleaños: ")
if (mes == "3" and dia >= "21") or (mes == "4" and dia <= "19"):
    print("tu signo es Aries")
elif (mes == "4" and dia >= "20") or (mes == "5" and dia <= "20"):
    print("tu signo es Tauro")
elif (mes == "5" and dia >= "21") or (mes == "6" and dia <= "20"):
    print("tu signo es Geminis")
elif mes == "6" and dia >= "21" or (mes == "7" and dia <= "22"):
    print("tu signo es Cancer")
elif mes == "7" and dia >= "23" or (mes == "8" and dia <= "22"):
    print("tu signo es Leo")
elif mes == "8" and dia >= "23" or (mes == "9" and dia <= "22"):
    print("tu signo es Virgo")
elif mes == "9" and dia >= "23" or (mes == "10" and dia <= "22"):
    print("tu signo es Libra")
elif mes == "10" and dia >= "23" or (mes == "11" and dia <= "21"):
    print("tu signo es Escorpio")
elif mes == "11" and dia >= "22" or (mes == "12" and dia <= "21"):
    print("tu signo es Sagitario")
elif mes == "12" and dia >= "22" or (mes == "1" and dia <= "19"):
    print("tu signo es Capricornio")
elif mes == "" and dia >= "20" or (mes == "2" and dia <= "18"):
    print("tu signo es Acuario")
elif mes == "2" and dia >= "19" or (mes == "3" and dia <= "20"):
    print("tu signo es Pisis")