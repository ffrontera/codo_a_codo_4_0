Algoritmo cinco_3
	//Dado un numero real L perteneciente al intervalo [1,10], la computadora
	//informa la cantidad de terminos de la serie armónica para satisfacer la 
	//desigualdad: 1 + 1/2 + 1/3 + 1/4 + ... 1/n > L
	
	Definir l, n Como Entero
	Definir sumatoria Como Real
	n = 0
	sumatoria = 0
	terminar = falso
	Escribir "Ingrese un número del 1 al 10:"
	Leer l
	Repetir
		n = n + 1
		sumatoria = sumatoria + 1/n
		Si sumatoria > l Entonces
			terminar = Verdadero
		FinSi
	Hasta Que terminar
	Escribir "La cantidad de terminos necesarios para cumplir con la desigualdad" 
	Escribir "1+1/2+1/3+..1/n>", l, " es de: ", n
FinAlgoritmo
