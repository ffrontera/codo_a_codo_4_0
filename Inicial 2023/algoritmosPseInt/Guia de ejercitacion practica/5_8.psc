Algoritmo cinco_8
	// En un colegio existe la posibilidad de elegir, en la materia "lengua extranjera", 
	// entre as siguientes opciones: [I]ngles, [F]rances, [P]ortugues y [A]leman. se ingresa,
	// para cada alumno, la lengua elegida. La computadora muestra el porcentaje de alumnos
	// que eligio cada lengua, en forma de numero y en forma grafica (histograma), utilizando
	// lineas hechas con asteriscos.
	
	Definir lenguaExtranjera, continuarIngresando Como Caracter
	Definir contadorTotalAlumnos, contadorI, contadorF, contadorP, contadorA Como Entero
	Definir porcentajeI, porcentajeF, porcentajeP, porcentajeA Como Real
	Definir error Como Logico
	
	contadorTotalAlumnos = 0
	contadorI = 0
	contadorF = 0
	contadorP = 0
	contadorA = 0
	
	Repetir
		contadorTotalAlumnos = contadorTotalAlumnos + 1
		
		Repetir
			error = Falso
			Escribir "Ingrese la eleccion del alumno en la materia lengua extranjera:"
			Escribir "[I]ngles - [F]rances - [P]ortugues - [A]leman"
			Leer lenguaExtranjera
			
			Segun lenguaExtranjera Hacer
				"I", "i":
					contadorI = contadorI + 1					
				"F", "f":
					contadorF = contadorF + 1					
				"P", "p":
					contadorP = contadorP + 1					
				"A", "a":
					contadorA = contadorA + 1					
				De Otro Modo:
					Escribir "Se ingreso una opcion no valida"
					error = Verdadero
			FinSegun
		Hasta Que !error
		
		Escribir "¿Continuar cargando alumnos?[S/N]"
		Leer continuarIngresando
	
	Hasta Que Minusculas(continuarIngresando) == "n" 
	
	porcentajeI = contadorI / contadorTotalAlumnos * 100
	porcentajeF = contadorF / contadorTotalAlumnos * 100
	porcentajeP = contadorP / contadorTotalAlumnos * 100
	porcentajeA = contadorA / contadorTotalAlumnos * 100
	
	Escribir "El porcentaje de alumnos por cada materia de lengua extranjera es:"
	Escribir "Ingles: ", porcentajeI, "% - Frances: ", porcentajeF, "% - Portugues: ", porcentajeP, "% - Aleman: ", porcentajeA, "%"
FinAlgoritmo
