Algoritmo cuatro_2
	//Dados dos numeros naturales b y e, la computadora muestra
	//el valor de b^e sinutilizar operadores o funciones que calculen
	//exponentes
	Definir b, e, resultado Como Entero
	Escribir "Vamos a calcular la potencia de un Número B elveado a un Número E"
	Escribir "Ingrese el valor de B"
	Leer b
	Escribir "Ingrese el valor de E"
	Leer e
	resultado = 1
	Mientras 0 < e Hacer
		resultado = resultado * b
		e = e - 1
	FinMientras
	Escribir "El resultado de la potencia es = ", resultado
	
FinAlgoritmo
