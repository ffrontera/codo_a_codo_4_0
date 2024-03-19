Algoritmo tres_4
	//escriba un programa que, dado el dato de cumpleaños del usuario(dia y mes), la computadora diga cual es su signo
	//del zodiaco.
	Definir dia, mes Como Entero
	Definir nombre Como Caracter
	Escribir "Escriba su nombre"
	Leer nombre
	Escribir "ingrese el dia (fecha) de su cumpleaños"
	Leer dia
	Escribir "ingrese el mes de su cumpleaños (en numero)"
	Leer mes
	
	Segun mes Hacer
		1:
			Si dia <= 19 Entonces
				Escribir "Hola ", nombre, " tu signo es Capricornio"
			SiNo
				Escribir "Hola ", nombre, " tu signo es Acuario"
			FinSi
		2:
			Si dia <= 18 Entonces
				Escribir "Hola ", nombre, " tu signo es Acuario"
			SiNo
				Escribir "Hola ", nombre, " tu signo es Piscis"
			FinSi
		3:
			Si dia <= 20 Entonces
				Escribir "Hola ", nombre, " tu signo es Piscis"
			SiNo
				Escribir "Hola ", nombre, " tu signo es Aries"
			FinSi
		4:
			
		5:
		6:
		7:
		8:
		9:
		10:
		11:
		12:
		De Otro Modo:
			Escribir "ERROR - a ingresado una opcion no valida"
	FinSegun
	
FinAlgoritmo
