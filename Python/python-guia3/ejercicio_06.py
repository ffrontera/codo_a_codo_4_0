frase = "El software es como el arte: la inspiración es importante, pero la técnica lo es todo"

arte = frase[23: 27]
ciencia = frase[47:57]
palabras = arte + " " + ciencia
print(arte)
print(ciencia)

importanteComienzo = frase.index("importante")
print(f"La palabra importante está en la posición {importanteComienzo} de la variable frase")
frase.lower()

a = frase.count("a") + frase.count("á")
print(f"La variable frase tiene {a} letras \"a\"")

e = frase.count("é") + frase.count("e")
i = frase.count("i") + frase.count("í")
o = frase.count("o") + frase.count("ó")
u = frase.count("u") + frase.count("ú")
vocales = a + e + i + o + u
print(f"La variable frase tiene {vocales} vocales.")

caracter = 0
for x in frase:
    if x.isalpha():
        caracter += 1
consonantes = caracter - vocales
print(f"La variable frase tiene {consonantes} consonantes.")