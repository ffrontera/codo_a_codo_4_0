Algoritmo cinco_6
	// Desarrollar un programa que pida un carácter al usuario y que por cada carga
	// pregunte si desea seduir ingresando. De la forma "¿Desea ingresar otro carácter?[S/N]".
	//La carga de datos finalizara cuando se detecta una n o N. La computadora debe mostrar 
	// la cantidad de letras vocales ingresadas. (Debe admitir mayúsculas y minúsculas)
	
	Definir letra, continuar Como Caracter
	Definir contadorVocales Como Entero
	
	contadorVocales = 0
	Mientras Minusculas(continuar) <> "n" Hacer
		Escribir "Ingrese un caracter seguido de la tecla enter"
		Leer letra
		
		Segun Minusculas(letra) Hacer
			"a", "e", "i", "o", "u":
				contadorVocales = contadorVocales + 1
		FinSegun
		
		Escribir "Desea seguir ingresando caracteres?[S/N]"
		Leer continuar
	FinMientras
	
	Escribir "Se ingresaron ", contadorVocales, " vocales."
FinAlgoritmo
