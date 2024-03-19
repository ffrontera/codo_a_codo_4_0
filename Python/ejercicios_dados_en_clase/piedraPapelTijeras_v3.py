# En esta versión, el programa no deberá preguntarle al usuario si quiere jugar una 
# partida más, sino que obligatoriamente se jugarán 6 partidas.
# ¿Qué modificaciones deberíamos hacer a la versión 2 ?

from random import randint

print("Vamos a jugar el clásico PIEDRA, PAPEL O TIJERAS!\nVamos a jugar 6 rondas:")

usuario_partidas = 0
computador_partidas = 0
partidas = 0
intentos_opcion = 0
while partidas < 6:
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
                computador_partidas += 1
            else:
                print("¡Ganaste! Piedra aplasta a Tijeras.")
                usuario_partidas += 1
        elif usuario_opc == "2":
            if computador_opc == "1":
                print("¡Ganaste! Papel envuelve a Piedra.")
                usuario_partidas += 1
            else:
                print("¡Perdiste! Tijeras corta Papel.")
                computador_partidas += 1
        elif usuario_opc == "3":
            if computador_opc == "1":
                print("¡Perdiste! Piedra aplasta Tijeras.")
                computador_partidas += 1
            else:
                print("¡Ganaste! Tijeras corta Papel.")
                usuario_partidas += 1
    partidas += 1    
print(f"Partidas ganadas por el usuario {usuario_partidas}\nPartidas ganadas por el computador {computador_partidas}")
print("Juego terminado.")            
