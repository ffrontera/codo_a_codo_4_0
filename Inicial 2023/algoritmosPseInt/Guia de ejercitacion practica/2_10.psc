Algoritmo dos_10
	//Dado un numero entero de hasta 4 dígitos, la computadora indica si es capicúa
	Definir num, a, b, c, d Como Caracter
	Definir largo Como Entero
	Escribir "Ingrese un número de dos, tres o cuatro dígitos"
	Leer num
	a = Subcadena(num,1,1)
	b = Subcadena(num,2,2)
	c = Subcadena(num,3,3)
	d = Subcadena(num,4,4)
	largo = Longitud(num)
	Si largo = 1 & largo > 4 Entonces
		Escribir "el numero ingresado no es valido"
	SiNo
		Si largo = 2 & a == b Entonces
			Escribir "El número ingresado es capicúa"
		SiNo
			Si largo = 3 & a == c Entonces
				Escribir "El número ingresado es capicúa"
			SiNo
				Si largo = 4 & a == d & b == c Entonces
					Escribir "El número ingresado es capicúa"
				SiNo
					Escribir "El número ingresado no es capicúa" 
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
