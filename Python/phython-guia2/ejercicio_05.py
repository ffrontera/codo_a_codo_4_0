saldo = 30000
print(f"Su saldo es de: ${saldo}")
while saldo > 0:
    retiro = int(input("¿Que cantidad de dinero desea extraer?: "))
    if retiro > saldo:
        print("¡Saldo insuficiente para realizar la operación!")
        print(f"Su saldo es de: ${saldo}")
    else:
        saldo = saldo - retiro
        print(f"Su saldo es de: ${saldo}")