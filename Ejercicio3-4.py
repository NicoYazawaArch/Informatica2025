"""
Escribir un programa que lea de teclado dos tiempos expresados en horas,
minutos y segundos, los sume y muestre por pantalla el resultado en horas, minutos y
segundos. El programa deberá utilizar las funciones del ejercicio anterior.

2: 3 : 5 --> segundos 1
1 : 59 : 59 --> segundos 2
"""
import en_clase_ejercicio_3_3

def main():
    h1=int(int(input("Ingrese el numero de horas: ")))
    m1=int(int(input("Ingrese el numero de minutos ")))
    s1=int(int(input("Ingrese el numero de segundos: ")))
    h2=int(int(input("Ingrese el numero de horas: ")))
    m2=int(int(input("Ingrese el numero de minutos ")))
    s2=int(int(input("Ingrese el numero de segundos: ")))
    
    segundos1=en_clase_ejercicio_3_3.hms_a_segtot(h1,m1,s1)
    segundos2=en_clase_ejercicio_3_3.hms_a_segtot(h2,m2,s2)
    segundos_totales= segundos1 + segundos2
    htotal, mtotal,stotal=en_clase_ejercicio_3_3.segtot_a_hms(segundos_totales)
    
    print(f"cantidad de segundos: {segundos_totales} ")
    print(f"El tiempo total: {htotal} horas, {mtotal} minutos, {stotal} segundos")
main()
