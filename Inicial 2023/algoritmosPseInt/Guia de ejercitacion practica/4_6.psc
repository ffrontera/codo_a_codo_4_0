Algoritmo cuatro_6
	//Se ingresan 5 números. La computadora muestra cuál fue el mayor y en que orden apareció
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
	Escribir "El mayor número ingresado fue: ", max, ". Y aparecion en el orden: ", aparicion
FinAlgoritmo
