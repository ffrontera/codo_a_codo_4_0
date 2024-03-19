Algoritmo cuatro_10
	//El usuario ingresa un valor N. Escriba un programa que calcule la suma de los cuadrados de los N primeros numeros naturales
	Definir n, acumulador Como Entero
	Escribir "ingrese un numero"
	Leer n
	acumulador = 0
	Para i = 1 Hasta n Hacer
		acumulador = acumulador + i^2
	FinPara
	Escribir "La suma de los cuadrados de los primeros ", n, " numeros naturales es: ", acumulador
FinAlgoritmo
