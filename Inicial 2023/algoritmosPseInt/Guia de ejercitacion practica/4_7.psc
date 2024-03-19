Algoritmo cuatro_7
	//Se ingresa un numero natural. La computadora muestra el factorial del numero.
	Definir num, factorial Como Entero
	Escribir "Ingrese el número al que quiera conocer su factorial:"
	Leer num
	factorial = 1
	Para i = 1 Hasta num Hacer
		factorial = factorial * i
	FinPara
	Escribir num, "! = ", factorial
FinAlgoritmo
