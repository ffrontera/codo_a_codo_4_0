precio = int(input("Ingrese el valor del articulo: "))
contado = precio * 0.9
ent_paln2 = (precio * 1.1) / 2
cuotas_plan2 = ent_paln2 / 2
ent_plan3 = (precio * 1.15) / 4
cuotas_plan3 = ((precio * 1.15) - ent_plan3) / 5
primeras_cuotas_plan4 = ((precio * 1.25) * 0.60) / 4
ultimas_cuotas_plan4 = (((precio * 1.25) - primeras_cuotas_plan4 * 4)) / 4
print(f"Opciones a pagar el articulo de precio: ${precio}")
print(f"Plan 1 - contado: ${contado}")
print(f"Plan 2 - entrega ${ent_paln2} y dos cuotas de ${cuotas_plan2}")
print(f"Plan 3 - entreda de ${ent_plan3} y cinco cuotas de ${cuotas_plan3}")
print(f"Plan 4 - Ocho cuotas, las rimers cuatro de ${primeras_cuotas_plan4}, y las 4 restantes de ${ultimas_cuotas_plan4}")
