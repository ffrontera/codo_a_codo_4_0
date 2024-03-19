lista_generos=["Acción","Animación","Comedia","Drama","Ciencia Ficción","Terror","Suspenso","Romántica"]
generos=[]

def imprimir_generos():
    for genero in range(0, len(lista_generos)):
       print(f"[{genero + 1}] - {lista_generos[genero]}")

def pelicula_generos():
  print("Seleccione un genero")
  imprimir_generos()
  otro ="s"
  while otro.lower() in ("s"):
      opcion_genero = input("> ")
      if not opcion_genero.isnumeric() :
         print("¡Opcion no válida! Debe ingresar un número")
         continue
      elif int(opcion_genero)-1 not in range(0, len(lista_generos)):
         print(f"¡Opcion no valida! Debe ingresar un numero 1 al {len(lista_generos)}")
         continue
      elif lista_generos[int(opcion_genero) - 1] in generos:
         print("¡El genero ingresado ya esta cargado!")
      else:
         generos.append(lista_generos[int(opcion_genero) - 1])
      otro=input("Desea ingresar otro género (S/N)?")
      while otro.lower()!="n" and otro.lower()!="s":
          otro=input("Opción inválida, ingrese S/N: ").lower()
      if otro.lower()== "n":
          return generos
pelicula_generos()

print(generos)
