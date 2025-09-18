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
    intentos=0
    contador=4
    password="Raze"
    #texto=input("Ingrese la contraseña de la billetera virtual: ")
    while intentos<contador:
        #print(f"Error contraseña incorrecta intentos restantes {contador} de {intentos} ")
        #time.sleep(1+intentos)
        texto=input("Vuelva a ingresar la contraseña de la billetera virtual: ")
        if texto == password:
            print(".................")
            print("Ingreso exitoso. Te podes robar 1000 BTC")
            return
        else:
            intentos+=1
            print(f"Error contraseña incorrecta intentos restantes {contador} de {intentos} ")
            time.sleep(1+intentos)
    
    print(".................")
    print("Ingresos excesivos sesion bloqueada.")


main()