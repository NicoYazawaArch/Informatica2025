"""
Ejercicio 4.6. Definir una función “cant_dias_mes” que, dados por parámetro dos números,
que representan el mes y el año, devuelva como resultado la cantidad de días
correspondientes al mes. En la definición se debe invocar a la función del enunciado 4.5.
"""
import Ejercicio4_5

def cant_dias_mes(mes,año):
    if mes == 2 and Ejercicio4_5.es_bisiesto(año):
        return 29
    elif mes == 2:
        return 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    else:
        return 31
""" 
def main():
    mes=int(input("Ingrese un mes: "))
    año=int(input("Ingrese año: "))
    print(f"El año la fecha tiene {cant_dias_mes(mes,año)} ")
main()
"""

