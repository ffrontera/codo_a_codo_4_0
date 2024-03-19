Algoritmo cinco_1
	//Se ingresan numeros hasta que se introduce un cero. la computadora mnuestra
	// el maximo y el minimo
	Definir num, min, max Como Real
	Definir bandera Como Logico
	Bandera = Verdadero
	min = 999999999
	Repetir
		Escribir "Ingrese un numero:"
		Leer num
		Si num == 0 Entonces
			bandera = Falso
		SiNo
			Si num < min Entonces
				min = num
			SiNo
				Si num > max Entonces
					max = num
				FinSi
			FinSi
		FinSi
	Hasta Que no bandera
	Escribir "El número minimo ingresado fue: ", min
	Escribir "El numero maximo ingresado fue: ", max
FinAlgoritmo
