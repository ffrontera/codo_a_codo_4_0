Algoritmo cinco_5
	// Una cuenta bancaria tien 30000 pesos de saldo. El usuario ingresará valores
	// que correspondan a extracciones via cajero automatico. Por cada extraccion se debe
	// mostrar como quedo el saldo luego de la operacion. Una extraccion que supere al 
	// saldo disponible se debe rechazar indicando que no es posible la operacion.
	// El programa finaliza cuando el saldo queda en 0.
	
	Definir saldo, extraccion Como Real
	Definir salir Como Logico
	continuar = Verdadero
	saldo = 30000
	
	Mientras continuar Hacer
		
		Limpiar Pantalla
		
		Escribir "Ingrese el valor a retirar:"
		Leer extraccion
		
	
		Si extraccion > saldo Entonces
			Escribir "No es posible realizar la operacion"
			Escribir "Su saldo es de: $", saldo
		SiNo
			saldo = saldo - extraccion
			Escribir "Su saldo es de: $", saldo
		FinSi
			
		Si saldo == 0 Entonces
			continuar = Falso
		FinSi
		
		Escribir "Pulse una tecla para continuar"
		Esperar Tecla
	FinMientras
	
	Limpiar Pantalla
	Escribir "Gracias por utilizar nuestros servicios"
FinAlgoritmo
