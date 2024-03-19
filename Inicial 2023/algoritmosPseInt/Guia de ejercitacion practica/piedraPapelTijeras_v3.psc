Algoritmo piedraPapelTijeras_v3
	
	Definir opcUsuario, opcComputadora, victoria, derrota, empate Como Entero
	
	Escribir "********************************************************************"
	Escribir "*                                                                  *"
	Escribir "*  ¡Bienvenido, vamos a jugar al clasico piedra, papel o tijeras!  *"
	Escribir "*                                                                  *"
	Escribir "********************************************************************"
	Escribir "*                  Vamos a recordar las reglas                     *"
	Escribir "*                                                                  *"
	Escribir "*                    - Piedra aplasta Tijeras                      *"
	Escribir "*                    - Papel envuelve Piedra                       *"
	Escribir "*                    - Tijeras corta Papel                         *"
	Escribir "********************************************************************"
	Escribir "Presione una tecla para continuar"
	Esperar Tecla
	Limpiar Pantalla
	
	victoria = 0
	derrota = 0
	empate = 0	
	Para i = 0 Hasta 5 Hacer
	Escribir "********************************************************************"
	Escribir "*                      Seleccione una opcion                       *"
	Escribir "********************************************************************"
	Escribir "* 1 - Piedra                                                       *"
	Escribir "* 2 - Papel                                                        *"
	Escribir "* 3 - Tijeras                                                      *"
	Escribir "********************************************************************"
	Leer opcUsuario
	opcComputadora = Azar(4)
	Limpiar Pantalla
	Escribir "********************************************************************"
	Segun opcUsuario Hacer
		1: 
			Escribir "*                         Elegiste Piedra                          *"
		2:
			Escribir "*                         Elegiste Papel                           *"
		3:
			Escribir "*                         Elegiste Tijeras                         *"
	FinSegun
	Segun opcComputadora Hacer
		1:
			Escribir "*                     Computadora elije Piedra                     *"
		2:
			Escribir "*                     Computadora elije Papel                      *"
		3:
			Escribir "*                     Computadora elije Tijeras                    *"
	FinSegun
	Escribir "********************************************************************"
	Segun opcUsuario Hacer
		1: //piedra
			Si opcComputadora == opcsuario Entonces //piedra
				Escribir "********************************************************************"
				Escribir "*               !Empate¡ - los dos eligieron Piedra                *"
				empate = empate + 1
			SiNo
				Si opcComputadora == 2 Entonces // papel
					Escribir "********************************************************************"
					Escribir "*               ¡Perdiste! - Papel envuelve a piedra               *"
					derrota = derrota +1
				SiNo //Tijeras
					Escribir "********************************************************************"
					Escribir "*               !Ganaste¡ - Piedra aplasta a Tijeras               *" 
					victoria = victoria + 1
				FinSi
			FinSi
		2: //papel
			Si opcComputadora == opcUsuario Entonces // papel
				Escribir "********************************************************************"
				Escribir "*                !Empate¡ - Los dos eligieron Papel                *"
				empate = empate + 1
			SiNo
				Si opcComputadora == 1 Entonces // piedra
					Escribir "********************************************************************"
					Escribir "*               ¡Ganaste! - Papel envuelve a Piedra                *"
					victoria = victoria + 1
				SiNo // Tijeras	
					Escribir "********************************************************************"
					Escribir "*                ¡Perdiste! - Tijeras corta a papel                *"	
					derrota = derrota + 1
				FinSi
			FinSi
		3: //tijeras
			Si opcComputadora == opcUsuario Entonces // tijeras
				Escribir "********************************************************************"
				Escribir "*               ¡Empate! - Los dos elijieron Tijeras               *"
				empate = empate + 1
			SiNo 
				Si opcComputadora == 1 Entonces //  Piedra
					Escribir "********************************************************************"
					Escribir "*              ¡Perdiste! - Piedra aplasta a Tijeras               *"
					derrota = derrota + 1
				SiNo // Papel
					Escribir "********************************************************************"
					Escribir "*                 ¡Ganaste! - Tijeras corta Papel                  *"
					victoria = victoria + 1
				FinSi
			FinSi
		De Otro Modo: // opcion fuera de rango
			Limpiar Pantalla
			Escribir "Ingresaste una opcion no valida"
	FinSegun
	Escribir "********************************************************************"
	Escribir "*                                                                  *"
	Escribir "*      El marcador es: Victorias: ", victoria, ". Derrotas: ", derrota, ". Empates: ", empate, ".      *"
	Escribir "*                                                                  *"
	Escribir "********************************************************************"
	Escribir "*                 Pulse una tecla para continuar                   *"
	Escribir "******************************************************************+*"
	Esperar Tecla
	
	Limpiar Pantalla
	FinPara

	Escribir "********************************************************************"
	Escribir "*                                                                  *"
	Escribir "*                         JUEGO TERMINADO                          *"
	Escribir "*                                                                  *"
	Escribir "*      Marcador final: Victorias: ", victoria, ". Derrotas: ", derrota, ". Empates: ", empate, ".      *"
	Escribir "*                                                                  *"
	Escribir "*                                                                  *"
	Si victoria > derrota Entonces
		Escribir "*                              GANASTE                              *"
	SiNo
		Si victoria < derrota Entonces
			Escribir "*                            PERDISTE                              *"
		SiNo
			Escribir "*                             EMPATE                               *"
		FinSi
	FinSi
	Escribir "********************************************************************"
	Escribir "*                 Gracias por jugar con nosotros =D                *"
	Escribir "********************************************************************"

FinAlgoritmo
