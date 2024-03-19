Algoritmo cinco_2
	//Se ingresan notas numericas de 0 a 10. El proceso de carga finaliza cuando
	//se detecta un numero fuera de rango( negativo o mayor a 10). La computadora
	//mnuestra el promedio de las notas
	Definir nota, sumatoria, cantidadDeNotas Como Entero
	Definir promedio Como Real
	Definir continuar Como Logico
	continuar = Verdadero
	sumatoria = 0
	cantidadDeNotas = 0
	Repetir
		Limpiar Pantalla
		Escribir "Ingrese una nota"
		Leer nota
		Si nota < 0 O nota > 10 Entonces
			continuar = Falso
		SiNo
			sumatoria = sumatoria + nota
			cantidadDeNotas = CantidadDeNotas + 1
		FinSi
	Hasta Que no continuar
	promedio = sumatoria / cantidadDeNotas
	Escribir "El promedio de las notas ingresadas es: ", promedio
FinAlgoritmo
