import Ejercicio4_6
"""
Definir una función “fecha_valida” que, dada por parámetros una fecha en
números (día, mes, año), devuelva un resultado booleano que indique si es válida o no.
¿Qué función debería invocar?
"""
def fecha_valida(dia,mes,año):
    if año <= 0:
        return False
    if mes < 1 or mes > 12:
        return False
    diasmes=Ejercicio4_6.cant_dias_mes(mes,año)
    
    if dia <= 1 or dia > diasmes:
        return False
    
    return True

"""def main():
    dia=int(input("Ingrese dia: "))
    mes=int(input("Ingrese mes: "))
    año=int(input("Ingrese año: "))
    if fecha_valida(dia,mes,año):
        print("La fecha es valida")
    else:
        print("La fecha es invalida")
main()"""