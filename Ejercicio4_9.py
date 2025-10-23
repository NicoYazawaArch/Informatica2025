import Ejercicio4_7
import Ejercicio4_6
"""
Ejercicio 4.9. Definir una función “dia_del_año” que reciba por parámetros tres números,
que representan el día, el mes y el año de una fecha, y devuelva como resultado la cantidad
de días transcurridos desde el comienzo del año (ejemplos, si la función recibe los números
17, 3 y 2025, debe devolver 76; si recibe los números 17, 3 y 2024, debe devolver 77). ¿Qué
función debería invocar?

"""
def dia_del_anio(dia,mes,año):
    total=0 #Valor acumulable para guardar valores 
    if Ejercicio4_7.fecha_valida(dia,mes,año): #Revisa si es la fecha valida si no lo es sigue adelante
        for m in range(1,mes): #El bucle itera la cantidad de dias en un mes y los suma en el valro total
            total+=Ejercicio4_6.cant_dias_mes(m,año)
        return total+dia 
    else:
        return "No valido"
    #return total+dia

def main():
    fecha1=dia_del_anio(17,3,2025)
    fecha2=dia_del_anio(17,3,2024)
    fecha3=dia_del_anio(90,13,9000)
    print(f"Cantidad de dias {fecha1} 'Debugg:Devolver 76 '")
    print(f"Cantidad de dias {fecha2} 'Debugg:Devolver 77 '")
    print(f"Cantidad de dias {fecha3} 'Debugg:Devolver error '")
main()