Algoritmo determinar_primo
	Definir contador Como Entero
	Definir numeroIngresado Como Entero
	Definir esPrimo Como Logico
	Escribir "Ingrse un número"
	leer numeroIngresado
	contador = 2 // el contador sera el divisor, arranco a buscar divisores desde el 2
	esPrimo = Verdadero
	Mientras (contador <= rc(numeroIngresado) & esPrimo) Hacer //el ciclo termina cuando no es primo o si se llega a la raiz del numero
		si (numeroIngresado % contador == 0) Entonces
			esPrimo = Falso // Si se encuentra un divisor
		FinSi
		contador = contador + 1
	FinMientras
	Si (esPrimo) Entonces
		Escribir "El número " , numeroIngresado , " es primo."
	SiNo
		Escribir "el número " , numeroIngresado , " no es primo."
	FinSi
FinAlgoritmo
