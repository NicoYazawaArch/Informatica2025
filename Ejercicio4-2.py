"""
Ejercicio 4.2. Definir y documentar una función denominada “val_abs”, que reciba un
número por parámetro y devuelva como resultado su valor absoluto. [No utilizar la función
abs () provista por Python]
"""
def val_abs(n):
    """La funcion verifica si el numero es negativo en cuyo caso lo devuele positivo"""
    if n<0:
        return -n
    else:
        return n
def main():
    valor=int(input("INgrese valor para convertir en absoluto: "))
    print(f"Resultado: {val_abs(valor)}")
main()

