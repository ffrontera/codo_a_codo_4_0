Algoritmo cinco_4
	// Se ingresan numeros hasta que la diferencia entre dos numeros consecutivos se repita.
	// La computadora muestra la cantidad de numeros ingresados
	
	Definir num, a, b Como Real
	Definir salir Como Logico
	Definir contador Como Entero
	
	Escribir "Vamos a ingresar números hasta que la diferencia entre dos números consecutivos se repita."
	saliir = Falso
	a = 0
	b = 0
	contador = 0	
	Repetir
		Escribir "Ingrese un número"
		Leer num
		
		Si num - a == a - b Entonces
			salir = Verdadero
		FinSi
		
		b = a
		a = num
		contador = contador + 1	
		Escribir "Llevas ingresados ", contador, " números"
	Hasta Que salir
	
FinAlgoritmo
