Algoritmo cinco_9
	// El ususario ingresa 12 valores, de a uno por vez, pertenecientes a sus sueldos
	// mensuales durante un año. La computaodra muestra su sueldo anual. Si durante la
	// carga de los sueldos mensuales se detecta un valor negarivo, esto indica que aun no
	// se ha cobrado el mes en curso, por lo tanto, debe  dejar de ingresarse datos y la 
	// computadora debe mostrar la sumatoria de los sueldos que se llevan cobrados.
	
	Definir sueldoMes, sumatoriaSueldos Como Real
	Definir mes Como Entero
	
	sumatoriaSueldos = 0
	mes = 0
	Repetir
		mes = mes + 1
		Escribir "Ingrese el sueldo correspondiente al mes ", mes, ":(Si aun no cobró el mes, ingrese el monto como negativo)"
		Leer sueldoMes
		Si sueldoMes >= 0 Entonces
			sumatoriaSueldos = sumatoriaSueldos + sueldoMes
		FinSi
	Hasta Que mes == 12 O sueldoMes < 0 
	
	Si mes == 12 Entonces
		Escribir "Su suedo anual fue de: $", sumatoriaSueldos
	SiNo
		mes = mes - 1
		Escribir "Su sueldo hasta el mes ", mes, " fue de: $", sumatoriaSueldos
	FinSi
FinAlgoritmo
