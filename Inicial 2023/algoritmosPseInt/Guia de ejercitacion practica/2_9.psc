Algoritmo dos_9
	Definir a, b, c Como Real
	Escribir "Ingrese la longitud del lado a del triangulo:"
	Leer a
	Escribir "Ingrese la longitud del lado b del triangulo:"
	Leer b
	Escribir "Ingrese la longitud del lado c del triangulo:"
	Leer c
	Si a + b < c O a + c < b O  b + c < a Entonces
		Escribir "El triangulo es inválido"
	SiNo
		Si a == b & b == c Entonces
			Escribir "El triangulo es equilatero"
		SiNo
			Si a <> b & b <> c & a <> c Entonces
				Escribir "El triangulo es escaleno"
			SiNo
				Escribir "El triangulo es isósceles"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
