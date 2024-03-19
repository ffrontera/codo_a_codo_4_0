# Tomando la versión 3 de base, ¿cómo deberíamos modificar el código para decidir 
# el número de partidas que queremos jugar PREVIAMENTE a comenzar el juego?
# El programa debería preguntarle al usuario cuántos partidos quiere jugar y luego 
# comenzar las partidas.

from random import randint

print("Vamos a jugar el clásico PIEDRA, PAPEL O TIJERAS!")
eleccion_partidas = int(input("Ingrese la cantidad de partidas que desea jugar: "))

usuario_partidas = 0
computador_partidas = 0
partidas = 0
intentos_opcion = 0
while partidas < eleccion_partidas:
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
            usuario_opc = "Piedra"
        elif usuario_opc == "2":
            usuario_opc = "Papel"
        else:
            usuario_opc = "Tijeras"
        if computador_opc == "1":
            computador_opc = "Piedra"
        elif computador_opc == "2":
            computador_opc = "Papel"
        else:
            computador_opc = "Tijeras"

        print(f"Tu elección fue {usuario_opc}, la elección de la computadora fue {computador_opc}")
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
