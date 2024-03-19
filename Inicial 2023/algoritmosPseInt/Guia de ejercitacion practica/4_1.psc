Algoritmo cuatro_1
	//Dado un entero N entre 1 y 10(inclusive), la computadora
	//lcomputadora muestra la tabla de multiplicar de N
	Definir num, control Como Entero
	Escribir "Ingrese un numero del 1 al 10 para conocer su tabla de multiplicar"
	Leer num
	control = 0
	Si num >= 0 y num <= 10 Entonces
		Escribir "La tabla del ", num, " es:"
		Mientras control < 11 Hacer
			Escribir num, " x ", control, " = ", (num * control)
			control = control + 1
		FinMientras
	SiNo
		Escribir "ERROR - El numero ingresado no es valido"
	FinSi	
FinAlgoritmo
