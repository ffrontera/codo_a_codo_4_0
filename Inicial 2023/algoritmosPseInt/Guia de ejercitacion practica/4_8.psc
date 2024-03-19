Algoritmo cuatro_8
	//Dados los numeros naturales A, B y C, la computadora muestra los multiplos de C
	//ubicados entre A y B (sin incluir los extremos)
	Definir a, b, c Como Entero
	Definir resto Como Real
	Escribir "vamos a calcuclar los multiplos de un numero C"
	Escribir "que esten comprendidos entre los numeros A y B"
	Escribir "Ingrece el valor de C"
	Leer c
	Escribir "ingrese el valor de A"
	Leer a
	Escribir "ingrese el valor de B"
	Leer b
	resto = 0
	Si a < b Entonces
		Para i = a + 1 Hasta b - 1 Hacer
			resto = i % c
			Si resto == 0 Entonces
				Escribir i
			FinSi
		FinPara
	SiNo
		Para i = b +1 Hasta a - 1 Hacer
			resto = i % c
			Si resto == 0 Entonces
				Escribir i
			FinSi
		FinPara
	FinSi
	
FinAlgoritmo
