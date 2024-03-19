Algoritmo cuatro_5
	//Dado un numero natural N, la computadora muestra los primeros N múltiplos de 3
	//excepto aquellos que sean a la vez multiplos de 5
	Definir n, contador, a Como Entero
	Escribir "Introduzca la cantidad de terminos que desea conocer de numeros"
	Escribir "que son multiplos de 3, pero no multiplos de 5"
	Leer n
	contador = 0
	a = 0
	Mientras contador < n Hacer
		Si a % 3 == 0 & a % 5 <> 0 Entonces
			Escribir a 
			contador = contador + 1
		FinSi
		a = a + 1
	FinMientras
FinAlgoritmo
