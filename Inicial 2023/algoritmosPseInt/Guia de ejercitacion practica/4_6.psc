Algoritmo cuatro_6
	//Se ingresan 5 n�meros. La computadora muestra cu�l fue el mayor y en que orden apareci�
	Definir num, max Como Real
	Definir aparicion Como Entero
	max = 0
	Para i = 1 Hasta 5 Hacer
		Escribir "Ingrese un numero:"
		Leer num
		Si num > max Entonces
			max = num
			aparicion = i
		FinSi
		Limpiar Pantalla
	FinPara
	Escribir "El mayor n�mero ingresado fue: ", max, ". Y aparecion en el orden: ", aparicion
FinAlgoritmo
