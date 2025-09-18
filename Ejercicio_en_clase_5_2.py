"""
 Escribir un programa:
a) que contenga una contraseña de 4 caracteres inventada, que le pregunte al usuario
la contraseña y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad ﬁja de
intentos. Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en
caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.
c) Modificar el programa anterior para que después de cada intento agregue una
pausa cada vez mayor, utilizando la función time.sleep(…) del módulo time
"""
import time
def main():
    cant=4
    intentos=0
    password="cas1"
    texto=input("Ingrese la contraseña: ")
    while password!=texto and intentos<cant:
        print("Contraseña incorrecta")
        time.sleep(1+intentos)
        texto=input("Ingrese la contraseña: ")
        intentos=intentos+1
        if texto== password:
            print("Eureka")
        else:
            print("Incorrecto")


main()