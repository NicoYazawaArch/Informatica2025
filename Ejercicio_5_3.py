"""
Ejercicio 5.3. Escribir un programa que elija un número al azar, entre 1 y 99, y lo mantenga
en secreto (utilice la función random.randrange (1,100) del módulo random). El programa
debe solicitar al usuario que adivine el número. Si el número que ingresa el usuario es
mayor, el programa debe responder "Incorrecto, mi número es menor"; si el número
ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". En
ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. Mostrar la
cantidad de intentos realizados para adivinar.
"""
import random
def main():
    intentos=1
    aleatorio=random.randrange(1,100)
    print(f"Debug: {aleatorio}")
    usuario=int(input("Ingrese un numero del 1 al 100 : "))
     # El bucle 'while' se ejecuta mientras el número del usuario no sea el aleatorio.
    while usuario!=aleatorio:
        # Aquí se evalúa si el número del usuario es mayor o menor.
        if usuario<aleatorio :
            print("Incorrecto, mi número es mayor.")
        else:
            print("Incorrecto mi numero es Menor")
        usuario=int(input("Incorrecto ingrese nuevamente numero del 1 al 100 : "))
        intentos += 1

    print(f"Correcto. Adivinaste el número {aleatorio} en {intentos} intentos.")
main()
