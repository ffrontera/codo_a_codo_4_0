Algoritmo tres_5
	//El usuario ingresa un número y la computadora le muestra su correspondiente representado
	//en número romano. nose debe ingresar un valor distinto de  1 , 5 , 10 , 50 , 100 , 500 , 1000
	Definir num Como Entero
	Escribir "Ingrese el número entero que quiera convertir a romano:"
	Leer num
	Segun num Hacer
		1:
			Escribir num, " en numero romano es: I"
		5:
			Escribir num, " en numero romano es: V"
		10:
			Escribir num, " en número romano es: X"
		50:
			Escribir num, " en número romano es: L"
		100:
			Escribir num, " en numero romano es: C"
		500:
			Escribir num, " en número romano es: D"
		1000:
			Escribir num, " en numero romano es: M"
		De Otro Modo:
			Escribir "El número ingresado no puede ser convertido por este programa :("
	FinSegun
FinAlgoritmo
