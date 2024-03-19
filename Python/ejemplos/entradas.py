nombre = input("Ingresa tu nombre: ") # a la variable le asignamos un input, entre parentesis el mensaje que indica
#lo que tiene que ingresar, em este caso pregunta el nombre
print(nombre)

num = input("ingresa un numero: ")
print("el doble del numero es: ")
print(num * 2) #en esta salida esperamos el doble del numero, pero lo que hace es concatenar cadenas
#esto es porque la instruccion input es para ingresar valores de cadenas
#para que la entrada sea numerica debemos usar la funcion float o int antes del input
# asi tambien para los otros tipos de datos int, float, str(este es por defecto, no hay que ponerlo) y bool
num =int(input("ingresa un numero: "))
print("El doble del numero es: ")
print(num * 2)  #aca vemos que se imprime el doble del numero ingresado