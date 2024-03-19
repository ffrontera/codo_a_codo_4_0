saldo = 30000
print(f"Su saldo es: {saldo} pesos.")
while saldo > 0:
    
    extraccion = float(input("Ingrese el monto de dinero a retirar: $"))
    if extraccion > saldo:
        print("Fondos insuficientes para realizar la operación.")
        print(f"Su saldo es: {saldo} pesos.")
    else:
        saldo = saldo - extraccion
        print(f"Su saldo es: {saldo} pesos")