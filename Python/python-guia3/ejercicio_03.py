frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
if letra in frase:
    print(f"La letra {letra} ESTÁ en la frase.")
else:
    print(f"La letra \"{letra}\" NO está en la frase.")