Algoritmo dos_7
	//Se ingresan tres números. La computadora los muestra ordenados de menor a mayor.
	Definir num1, num2, num3 Como Real
	Escribir "Ingrese tres números, cada uno seguido de la tecla Enter"
	Leer num1, num2, num3
	Escribir Sin Saltar "Los numero ingresados ordenados de menor a mayor son: "
	Si num1 > num2 & num1 > num3 & num2 > num3 Entonces
		Escribir num3, ", " num2, ", " num1
	SiNo
		Si num1 > num2 & num1 > num3 & num2 < num3 Entonces
			Escribir num2, ", ", num3, ", ", num1
		SiNo
			Si num1 < num2 & num1 > num3 & num2 > num3 Entonces
				Escribir num3, ", ", num1, ", " num2
			SiNo
				Si num1 < num2 & num1 < num3 & num2 > num3 Entonces
					Escribir num1, ", " num3, ", " num2
				SiNo
					Si num1 > num2 & num1 < num3 & num2 < num3 Entonces
						Escribir num2, ", " num1, ", " num3
					SiNo
						Escribir num1, ", " num2, ", " num3
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
