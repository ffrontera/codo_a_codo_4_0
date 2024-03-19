#TODO: Es un comentario que recuerda que tengo que hacer
# def generar_usuario(nombre, apellido):
#     usuario = nombre[0].lower() + apellido.replace(" ", "").lower()
#     return usuario

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# nombre_usuario = generar_usuario(nombre, apellido)
# print(f"Su nombre de usuario es: {nombre_usuario}")


# def contar_vocales(texto):
#     cantidad_vocales = 0
#     vocales = "aáeéiíoóuú"
#     TODO: Calcular la cantidad de vocales
#     for letra in texto.lower():
#         if letra in vocales:
#             cantidad_vocales += 1
#     return cantidad_vocales

# frase = input("Ingrese una frase: ")
# total = contar_vocales(frase)
# print(f"En la frase hay {total} vocales")


# from random import randint
# def tirar_dados():
#     num1 = randint(1, 6)
#     num2 = randint(1, 6)
#     return (num1, num2)

# jugador1 = tirar_dados()
# jugador2 = tirar_dados()
# jugador3 = tirar_dados()
# print(jugador1, jugador2, jugador3)


# 1) Generar un nombre de usuario único: Escribe una función que tome un nombre y un apellido como parámetros, 
# y genere un nombre de usuario único concatenando la primer letra del nombre y el apellido.
# La función deberá llamarse generar_usuario y recibirá dos parámetros: nombre y apellido.
# Ingrese su nombre: Juan
# Ingrese su apellido: Perez
# Su nombre de usuario será: jperez

# def generador_usuario(nombre, apellido):
#     usuario = nombre[0].lower() + apellido.replace(" ", "").lower()
#     return usuario

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# usuario = generador_usuario(nombre, apellido)
# print(f"Su usuario es: {usuario}")


# 2) Crea una función contar_vocales que reciba una cadena de texto y devuelva el número total de vocales que tiene la cadena. 
# Ingrese un oracion: Las funciones son una parte fundamental de programación
# La oración tiene 20 vocales.

# def contar_letras(cadena_texto, letras_buscadas):
#     cantidad_coincidencias = 0
#     for letra in cadena_texto.lower():
#         if letra in letras_buscadas.lower():
#             cantidad_coincidencias += 1
#     return cantidad_coincidencias
# texto = input("ingrese una frase: ")
# busqueda = input("Ingrese las letras a buscar sin espacio: ")
# cantidad_letras = contar_letras(texto, busqueda)
# print(f"La cantidad de letras \"{busqueda}\" en el texto es de: {cantidad_letras}")


# 3) Crear una función tirar_dados que devuelva el resultado de tirar dos dados. Los números deberán retornar en una tupla.
# Mostrar en pantalla el resultado de los dos dados.
# El resultado de tirar los dados es: 5 y 3

# from random import randint
# def tirar_dados():
#     dado_1 = randint(1, 6)
#     dado_2 = randint(1, 6)
#     return (dado_1, dado_2)

# print(tirar_dados())


# 4) Escribir una función llamada calcular_impuesto que tome dos argumentos: el ingreso anual y la tasa impositiva. 
# La función debe calcular la cantidad de impuestos que una persona debe pagar y devolverla. Luego, escribe un programa
# que solicite al usuario ingresar su ingreso anual y la tasa impositiva, y luego muestre la cantidad de impuestos que deben pagarse.
# ¿Cuál es el ingreso anual en $?: 3500000
# ¿Cuál es la tasa impositiva en %?: 12
# El impuesto a pagar es: $420000.00

# def calcular_impuesto(ingreso_anual, tasa_impositiva):
#     impuesto = (ingreso_anual * tasa_impositiva) / 100
#     return round(impuesto, 2)
# ingreso = int(input("¿Cual es su ingreso anual en pesos?:"))
# tasa = int(input("¿Cual es la tasa impositiva en %?: "))
# impuesto = calcular_impuesto(ingreso, tasa)
# print(f"El impuesto a pagar es: {impuesto}")


# 5) Escribe una función llamada es_contrasenia_segura que tome una cadena (contraseña) como argumento y determine si es segura. 
# Verificaremos que la contraseña sea segura si:
#        - Tiene al menos 8 caracteres.
#        - Contiene al menos una letra mayúscula
#        - Contiene al menos una letra minúscula
#        - Contiene al menos un número. 
# La función debe devolver True si la contraseña es segura y False en caso contrario.
# Luego, escribir un programa que solicite al usuario ingresar una contraseña y utilice la función para verificar su seguridad.
# Ingrese una contraseña: Psowj3e2		Ingrese una contraseña: jiueorwe
# Su contraseña es segura.			Su contraseña NO es segura.

# def es_contrasenia_segura(contrasenia):
#     #largo al menos 8
#     if len(contrasenia) < 8:
#         return False
#     # al menos 1 mayuscula
#     if contrasenia.islower():
#         return False
#     # al menos una minuscula
#     if contrasenia.isupper():
#         return False
#     #al menos un número
#     if contrasenia.isalpha():
#         return False
#     # es segura
#     return True
# password = input("Ingrese contraseña: ")
# if es_contrasenia_segura(password):
#     segura = '"SEGURA"'
# else:
#     segura = '"NO SEGURA"'
# print(f"La contraseña ingresada es {segura}")


# 6) Crear una función que se llame calcular_promedio, que reciba por parámetro una lista de números enteros.
# La función debe calcular el promedio y devolver el resultado. Con el resultado de esa función se deberá llamar
# a una nueva función imprimir_nota, que debe recibir por parámetro el promedio e imprimir un mensaje al usuario de 
# acuerdo a la siguiente tabla:
# Si la nota es menor a 4 deberá imprimir: 
# “Su promedio es de {promedio}. No es suficiente para aprobar la carrera”
# Si la nota es igual o mayor a 4 y menor a 7: 
# “Su promedio es de {promedio}. Es suficiente para aprobar la materia”
# Si la nota es igual o mayor a 7 y menor a 9: 
# “Su promedio  es de {promedio}. Le permite solicitar una beca del 50%”
# Si la nota es igual o mayor a 9: 
# “Su promedio es de {promedio}.Le permite solicitar una beca del 100%”
# Aclaración: La lista de números enteros puede ser solicitada al usuario en tiempo real, o pre cargada en el código.

def calcular_promedio(numeros):
    sumatoria = 0
    for numero in range(0, len(numeros)):
        sumatoria += numeros[numero]
    else:
        return round(sumatoria / len(numeros), 2)

def imprimir_nota(nota):
    if nota < 4:
        print(f"Su promedio es de {nota}. No es suficiente para aprobar la carrera")
    elif nota >= 7 and nota < 7:
        print(f"Su promedio es de {nota}. Es suficiente para aprobar la materia")
    elif nota >= 7 and nota < 9:
        print(f"Su promedio  es de {nota}. Le permite solicitar una beca del 50%")
    else:
        print(f"Su promedio es de {nota}.Le permite solicitar una beca del 100%")

lista_notas = []
agregar = True
while agregar:
    nota = int(input("Ingrese una nota: "))
    lista_notas.append(nota)
    continuar = input("¿Desea agregar otra nota?[S/N]: ").lower()
    if continuar == "n":
        agregar = False
promedio = calcular_promedio(lista_notas)
imprimir = imprimir_nota(promedio)