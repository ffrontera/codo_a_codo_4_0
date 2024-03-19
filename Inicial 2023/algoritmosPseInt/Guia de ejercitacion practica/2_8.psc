Algoritmo dos_8
	//Dados dos nuemros enteros, la computadora indica si el mayor es divisible por el menor
	Definir num1, num2, resto1, resto2 Como Entero
	Escribir "Ingrese un numero entero"
	Leer num1
	Escribir "Ingrese otro numero entero"
	Leer num2
	resto1 = num1 % num2
	resto2 = num2 % num1
	Si num1 > num2 Entonces
		Si resto1 == 0 Entonces
			Escribir "El numero mayor es divisible por el menor"
		SiNo
			Escribir "El numero mayor No es divisible por el menor"
		FinSi
	SiNo
		Si resto2 == 0 Entonces
			Escribir "El numero mayor es divisible por le menor"
		SiNo
			Escribir "El numero mayor no es divisible por el menor"
		FinSi
	FinSi
FinAlgoritmo
