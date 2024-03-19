Algoritmo cuatro_4
	//Dado un número N, la PC muestra los primeros N términos de la sucesión de Fibonacci
	//0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
	Definir n, a, b, c, contador Como Entero
	Escribir "Defina la cantidad de terminos a conocer de la sucesión de Fibonacci"
	Leer n
	a = 0
	b = 1
	contador = 3
	Si n == 1 Entonces
		Escribir a
	SiNo
		Si n == 2 Entonces
			Escribir a
			Escribir b
		SiNo
			Escribir a
			Escribir b
			Mientras contador <= n Hacer
				c = a + b
				Escribir c
				a = b
				b = c
				contador = contador + 1
			FinMientras
		FinSi
	FinSi
FinAlgoritmo
