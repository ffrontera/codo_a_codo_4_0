import random

print("Vamos a jugar a Piedra, Papel o Tijeras :D")


continuar = True
while continuar:
    mi_eleccion = int(input("Elejir: [1]piedra, [2]Papel o [3]Tijeras"))
    pc_opcion = random.randint(1, 3)

    if mi_eleccion == pc_opcion:
        print("Empate")
    elif mi_eleccion == 1: #Piedra
        if pc_opcion == 2: #Papel
            print("Papel envuelve Piedra. Gano la computadora.")
        else: # Tijeras
            print("Piedra aplasta Tijeras. Ganaste.")
    elif mi_eleccion == 2: #Papel
        if pc_opcion == 1: #piedra
            print("Papel enuelve a Piedra. Ganaste.")
        else: #Tijeras
            print("Tijeras corta Papel. Gana la computadora.")
    elif mi_eleccion == 3: #Tijeras
        if pc_opcion == 1: # Piedra
            print("Piedra apasta a Tijeras. Gana la computadora.")
        else: #Papel
            print("Tijeras corta papel. Ganaste.")
    else:
        print("El valor ingresado no es válido.")
        