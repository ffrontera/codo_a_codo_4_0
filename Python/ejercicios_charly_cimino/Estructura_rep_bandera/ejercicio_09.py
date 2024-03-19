sueldo_mes = 0
mes = 1
sumatoria_sueldos = 0
continuar = True
while mes <= 12 and continuar:
    if mes == 1:
        mes_str = "Enero"
    elif mes == 2:
        mes_str = "Febrero"
    elif mes == 3:
        mes_str = "Marzo"
    elif mes == 4:
        mes_str = "Abril"
    elif mes == 5:
        mes_str = "Mayo"
    elif mes == 6:
        mes_str == "Junio"
    elif mes == 7:
        mes_str = "Julio"
    elif mes == 8:
        mes_str = "Agosto"
    elif mes == 9:
        mes_str = "Septiembre"
    elif mes == 10:
        mes_str = "Octubre"
    elif mes == 11:
        mes_str = "Noviembre"
    else:
        mes_str = "Diciembre"
    
    sueldo_mes = float(input(f"Ingrese su sueldo del mes {mes_str}: "))
    if sueldo_mes >= 0:
        sumatoria_sueldos += sueldo_mes
        mes += 1
    else:
        continuar = False

print(f"Las suma de sus sueldos al mes de {mes_str} es: ${sumatoria_sueldos}")