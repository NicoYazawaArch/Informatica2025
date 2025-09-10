"""
Ejercicio 4.8. Definir una función “fecha_siguiente” que, dada por parámetros una fecha en
números (día, mes, año), devuelva como resultado la fecha (día, mes, año) del día siguiente.
"""
import Ejercicio4_7
import Ejercicio4_6
def fecha_siguiente(dia,mes,año):
    if not Ejercicio4_7.fecha_valida(dia, mes, año):
        return False
    dias_del_mes = Ejercicio4_6.cant_dias_mes(mes,año)
    
    if dia < dias_del_mes:
        dia += 1
    elif dia == dias_del_mes and mes < 12:
        dia = 1
        mes += 1

    elif dia == dias_del_mes and mes == 12:
        dia = 1
        mes = 1
        año += 1
    else:
        return False
    
    return dia,mes,año

def main():
    dia=int(input("Ingrese dia: "))
    mes=int(input("Ingrese mes: "))
    año=int(input("Ingrese año: "))
    if fecha_siguiente(dia,mes,año):
        print("Fecha siguiente: ", fecha_siguiente(dia,mes,año))
    else:
        print("Fecha invalida")


main()
