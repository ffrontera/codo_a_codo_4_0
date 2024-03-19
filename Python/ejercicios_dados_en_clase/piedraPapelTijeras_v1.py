# Recordando el juego clásico de Piedra, Papel o Tijera crear un algoritmo que 
# permita:
# - Ingresar al usuario Piedra (1), Papel (2), Tijera (3) 
# - Que el computador elija una opción al azar.
# - En base al resultado de la elección del usuario y del computador, el 
# computador imprima que seleccionó el usuario, el computador y quien ganó.

from random import randint

print("Vamos a jugar el clásico PIEDRA, PAPEL O TIJERAS!")

usuario_opc = ""
intentos_opcion = 0
while usuario_opc != "1" and usuario_opc != "2" and usuario_opc != "3":
    usuario_opc = input("Elija su opción: [1]Piedra, [2]Papel o [3]Tijeras ")
    intentos_opcion += 1
    if intentos_opcion == 3 and usuario_opc != "1" and usuario_opc != "2" and usuario_opc != "3":
        print("Te quedaste sin intentos")
        break    
    elif intentos_opcion < 3 and usuario_opc != "1" and usuario_opc != "2" and usuario_opc != "3":
        print(f"Ingresaste una opción no válida. Te quedan {3 - intentos_opcion} intentos.")    
    else:
        computador_opc = str(randint(1, 3))

        if usuario_opc == "1":
            usuario = "Piedra"
        elif usuario_opc == "2":
            usuario = "Papel"
        else:
            usuario = "Tijeras"
        if computador_opc == "1":
            computador = "Piedra"
        elif computador_opc == "2":
            computador = "Papel"
        else:
            computador = "Tijeras"

        print(f"Tu elección fue {usuario}, la elección de la computadora fue {computador}")
        if usuario_opc == computador_opc:
            print(f"¡Empate!")
        elif usuario_opc == "1":
            if computador_opc == "2":
                print("¡Perdiste! Papel envuelve a Piedra.")
            else:
                print("¡Ganaste! Piedra aplasta a Tijeras.")
        elif usuario_opc == "2":
            if computador_opc == "1":
                print("¡Ganaste! Papel envuelve a Piedra.")
            else:
                print("¡Perdiste! Tijeras corta Papel.")
        elif usuario_opc == "3":
            if computador_opc == "1":
                print("¡Perdiste! Piedra aplasta Tijeras.")
            else:
                print("¡Ganaste! Tijeras corta Papel.")

print("Juego terminado.")            