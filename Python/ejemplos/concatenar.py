nombre = input("Ingresa tu nombre ")
print("Hola ", nombre, "!!!") #concatenamos con comas
print("Hola", nombre, "!!!", sep=" ") #aca ponemos que hay un espacio entre cada dato concatenado
# este es el valor por defecto, como vemos en el primer print al dejar un espacio luego del hola
# la consola muestra dos espacios en la separacion. En la siguiente print vemos como seria para que quede 
# si le ponemos un espacio al final de la cadena(o de cada valor)
print("hola ",nombre,"!!!", sep="")
#tabien podemos poner caracteres para separar
print("Hola",nombre,"!!!", sep="***")

#para concatenar al asignar una variable debemos usar el signo +
# de otro modo tendremos resultados no deseados. Ej
salida = "hola " , nombre, "!!!" #Esto en python es una estructura de datos
print(salida)
salida = "hola " + nombre + "!!!" # al usar el signo de mas debemos escribir los espacios literalmente
print(salida)

#para asignar una concatenacion entre una cadena y una variable del tipo numerica, primero debemos convertir
#la variable numeria en cadena.
edad = int(input("ingresa tu edad "))
print(edad)
salida = "Tenes: " + str(edad) + " años"
print(salida)
#si usamos la concatenacion dentro de un print no tendremos ese problema
print("tenes ",edad," años")
