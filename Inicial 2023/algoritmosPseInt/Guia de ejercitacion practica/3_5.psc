Algoritmo tres_5
	//El usuario ingresa un n�mero y la computadora le muestra su correspondiente representado
	//en n�mero romano. nose debe ingresar un valor distinto de  1 , 5 , 10 , 50 , 100 , 500 , 1000
	Definir num Como Entero
	Escribir "Ingrese el n�mero entero que quiera convertir a romano:"
	Leer num
	Segun num Hacer
		1:
			Escribir num, " en numero romano es: I"
		5:
			Escribir num, " en numero romano es: V"
		10:
			Escribir num, " en n�mero romano es: X"
		50:
			Escribir num, " en n�mero romano es: L"
		100:
			Escribir num, " en numero romano es: C"
		500:
			Escribir num, " en n�mero romano es: D"
		1000:
			Escribir num, " en numero romano es: M"
		De Otro Modo:
			Escribir "El n�mero ingresado no puede ser convertido por este programa :("
	FinSegun
FinAlgoritmo
