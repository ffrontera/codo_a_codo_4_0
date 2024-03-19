Algoritmo tres_1
	//Escribir un programa que simule una calculadora basicaque realice operaciones de 
	//suma, resta, multiplicacion y division. se debe recibir come entrada dos numeros reales
	//y un operador, que puede ser +, - , * ó /. la salida del programa debe ser el resultado
	// de la operación
	Definir a, b Como Real
	Definir continuar, op Como Caracter
	Definir resultado Como Real
	Repetir
		Escribir "Ingrese un número A"
		leer a
		Escribir "Elija una opereción matematica a realizar para A B"
		Escribir "[+] Suma"
		Escribir "[-] Resta"
		Escribir "[*] Multiplicacion"
		Escribir "[/] Divición"
		Leer op
		Escribir "Ingrese un número B"
		Leer b
		Segun op Hacer
			"+": //Suma
				resultado = a + b
				Escribir "El resultado de la suma es: ", Resultado
			"-": //Resta
				resultado = a - b
				Escribir "El resultado de la resta es: ", resultado
			"*": //Multiplicacion
				resultado = a * b
				Escribir "El resultado de la multiplicacion es: ", resultado
			"/": //Division
				resultado = a / b
				Escribir "El resultado de la division es: ", resultado
			De Otro Modo:
				Escribir "Error - Opción no valida"
		FinSegun
		Escribir "Para continuar haciendo operaciones matematicas presione enter"
		Escribir "De lo contrario escriba no"
		Leer continuar
		Limpiar Pantalla
	Hasta Que Minusculas(continuar) == "no"
	Escribir "Saludos"
FinAlgoritmo
