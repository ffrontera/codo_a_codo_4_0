america_del_sur = ('Perú', 'Uruguay', 'Venezuela', 'Guyana', 'Paraguay', 'Chile', 'Brasil', 'Ecuador', 'Bolivia', 'Surinam', 'Colombia', 'Argentina')

pais = input("Ingrese un pais: ").capitalize()

if pais in america_del_sur:
    print(f"{pais} pertenece a América del Sur.")
else:
    print(f"{pais} no pertenece a América del Sur.")