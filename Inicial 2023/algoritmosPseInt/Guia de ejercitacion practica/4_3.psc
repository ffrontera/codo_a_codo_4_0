Algoritmo cuatro_3
	//Dada la cantidad de términos a considerar entre los paréntesis, la computadora
	//muestra el valor de la correspondiente aproximación de Pi descubierta por Leibniz.
	// 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + 1/n) = Pi
	Definir n, contador Como Entero
	Definir resultadoParaPi, resultadoParaIteracion Como Real
	Escribir "Ingrese la cantidad de iteraciónes que desea ejecutar para el calculo de Pi"
	Escribir "Segun la formula de Leibniz"
	Leer n
	contador = 0
	resultadoParaIteracion = 0
	Mientras contador <= n Hacer
		resultadoParaIteracion = ((-1)^contador) / ((2 * contador) + 1) + resultadoParaIteracion
		contador = contador + 1
	FinMientras
	resultadoParaPi = 4 * resultadoParaIteracion
	Escribir "Para ", n, " iteraciones de la formula de Leibniz El valor de Pi es: ", resultadoParaPi
FinAlgoritmo
