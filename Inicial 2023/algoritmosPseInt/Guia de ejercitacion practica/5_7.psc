Algoritmo cinco_7
	// Desarrollar un programa que pida una cantidad de articulos comprados y el precio
	// unitario de ese articulo. Por cada carga debe preguntar si se desea seguir
	// ingresando de la forma "¿Desea ingresar otro articulo?[S/N]". La carga de datos
	// Finaliza cuando se detecta una n o N. La computadora debe mostrar el monto de la 
	// factura
	
	Definir precioUnitario, totalFactura Como Real
	Definir cantidadArticulo Como Entero
	Definir continuarIngresando Como Caracter
	
	totalFactura = 0
	Repetir
		Escribir Sin Saltar "Ingrese cantidad de articulos: "
		Leer cantidadArticulo
		Escribir Sin Saltar "Ingrese el precio unitario: "
		Leer precioUnitario
		
		totalFactura = totalFactura + (cantidadArticulo * precioUnitario)
		
		Escribir "¿Desea ingresar otro articulo?[S/N]"
		Leer continuarIngresando
		
	Hasta Que Minusculas(continuarIngresando) == "n" 
	
	Escribir "El monto total de la factura es: $ ", totalFactura
FinAlgoritmo
