from random import randint

x = randint(1, 100)
y = randint(1, 100)

if x == y:
    print("Estás de suerte, los dos números coinciden.")
elif x > y:
    print(f"El número {x} es mayor que el número {y}.")
else:
    print(f"El número {y} es mayor que el número {x}.")