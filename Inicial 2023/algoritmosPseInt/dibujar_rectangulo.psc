Algoritmo dibujar_rectangulo
	Definir ancho Como Real
	Definir alto Como Real
	Definir filas Como Entero
	Definir columnas Como Entero
	filas = 0
	columnas = 0
	ancho = 0.1
	Mientras (trunc(ancho) <> ancho | ancho <= 0) Hacer
		Escribir "Ingrese ancho (valor entero)"
		Leer ancho
	FinMientras
	alto = 0.1
	Mientras (trunc(alto) <> alto | alto <= 0) Hacer
		Escribir "Ingrese alto (valor entero)"
		Leer alto
	FinMientras
	Mientras (filas < alto) Hacer
		Mientras (columnas < ancho) Hacer
			Escribir Sin Saltar "*"
			columnas = columnas + 1
		FinMientras
		Escribir ""
		filas = filas + 1
		columnas = 0
	FinMientras
FinAlgoritmo