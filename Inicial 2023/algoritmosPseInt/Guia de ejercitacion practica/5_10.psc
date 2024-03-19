Algoritmo cinco_10
	// El usuario ingresa un numero entero mayor que uno. Si el numero ingresado es
	// incorrecto, volver a pedirselo. La computadora indica si el numero ingresado es 
	// primo o no.
	
	Definir n Como Entero
	Definir resto Como Real
	Definir validacionNumero Como Logico
	
	validacionNumero = Falso
	Repetir
		Escribir "Ingrese un número mayor entero mayor a 1"
		Leer n
		Si n >= 2 Entonces
			validacionNumero = Verdadero
		SiNo
			Escribir "El número ingresado es incorrecto."
		FinSi
	Hasta Que validacionNumero
		
	Para i = 2 Hasta n - 1 Hacer
		resto = n % i
		Si resto == 0 Entonces
			Escribir "El numero ingresado no es primo"
			i = n - 1
		FinSi
	FinPara
	Si resto <> 0 Entonces
		Escribir "El número ingresado es primo"
	FinSi
	
FinAlgoritmo
