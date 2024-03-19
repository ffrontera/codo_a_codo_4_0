Algoritmo mayor_menor_igual
	Definir cartaActual Como Entero
	Definir proxCarta Como Entero
	Definir opc Como Entero
	Definir puntaje Como Entero
	Definir opcionValida Como Logico
	Definir fueDerrotado Como Logico
	Escribir "Bienvenido a MAYOR-MENOR-IGUAL"
	Escribir "La computadora genera un numero al azar entre 1 y 12."
	Escribir "Deber�s predecir si el pr�ximo n�mero ser� MAYOR, MENOR O IGUAL."
	Escribir "Cada acierto vale 1 punto. El juego termina cuando no adivin�s."
	Escribir ""
	Escribir "Precion� cualquier tecla para continuar..."
	Esperar Tecla
	Limpiar Pantalla
	fueDerrotado = Falso //Inicializacion de la bandera
	puntaje = 0  //Inicializaci�n del puntaje
	cartaActual = azar(12) + 1 //Genero la primer carta
	Mientras (!fueDerrotado) Hacer //Termina cuando sea derrotado
		opcionValida = Falso // Inicializacion de la bandera
		proxCarta = azar(12) + 1 //Se piensa la carta que saldr�
		Mientras (!opcionValida) Hacer //terminara si la opcion es valida
			Escribir "salio el [ " , cartaActual , " ]" 
			Escribir "" //linea en blanco
			Escribir "La pr�xima carta ser�:"
			Escribir "" //linea en blanco
			Escribir "[1] MAYOR"
			Escribir "[2] MENOR"
			Escribir "[3] IGUAL"
			Escribir ""
			Escribir "Escrib� la opci�n correspondiente."
			Leer opc
			Escribir "" //linea en blanco
			Segun (opc) Hacer
				1: //mayor
					Si (proxCarta > cartaActual) Entonces
						Escribir "Acertaste. Salio el " , proxCarta
						puntaje = puntaje + 1 // se suma un punto
					SiNo
						Escribir "Perdiste. Salio el " , proxCarta
						fueDerrotado = Verdadero // bandera
					FinSi
					opcionValida = Verdadero // bandera
				2:	// menor
					Si (proxCarta < cartaActual) Entonces
						Escribir "Acertaste. Salio el " , proxCarta
						puntaje = puntaje + 1 //suma 1 punto
					SiNo
						Escribir "Perdiste. Salio el " , proxCarta
						fueDerrotado = Verdadero //bandera
					FinSi
					opcionValida = Verdadero //bandera
				3: //igual
					Si (proxCarta = cartaActual) Entonces
						Escribir  "Acertaste. Salio el " , proxCarta
						puntaje = puntaje + 1 //suma 1 punto
					SiNo
						Escribir "Perdiste. Salio el " , proxCarta
						fueDerrotado = Verdadero //bandera
					FinSi
					opcionValida = Verdadero //bandera
				De Otro Modo:
					   Escribir "Opcion invalida" 					
			   FinSegun
			   Escribir "" //linea en blanco
		   FinMientras
		   Escribir "Precion� una tecla para continuar..."
		   Esperar Tecla
		   Limpiar Pantalla
		   cartaActual = proxCarta //la carta que salio ahora es la actual
	   FinMientras
	   Escribir "Tu puntuaci�n: " , puntaje
FinAlgoritmo
