Algoritmo dos_6
	//Dada la cantidad de alumnos de un curso y la cantidad de sillas disponibles
	//La computadora indica si alcazan las sillas, en caso contrario, indica cuantas faltan
	//para que todo el alumnado tenga asiento
	Definir alumnos, sillasTotales, sillasFaltantes Como Entero
	Escribir "Ingrese la cantidad de alumnos que asisten al curso:"
	Leer alumnos
	Escribir "Ingrese la cantidad de sillas disponibles en el aula:"
	Leer sillasTotales
	Si alumnos > sillasTotales Entonces
		sillasFaltantes = alumnos - sillasTotales
		Escribir "Las lugares en el aula son insuficientes, faltan ", sillasFaltantes, " sillas."
	SiNo
		Escribir "El aula cuenta con la cantidad de sillas necesarias para el alumnado."
	FinSi
FinAlgoritmo
