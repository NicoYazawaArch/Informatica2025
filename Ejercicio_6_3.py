"""
Ejercicio 6.3. Definir una función que reciba una cadena de caracteres como parámetro y
devuelva como resultado la cadena invertida. (Ej: para el argumento ‘Hola Undav!’ debería
devolver al programa principal ‘!vadnU aloH’. No utilizar segmento de cadena [ : : -1 ] )

"""

def invert(cadena):
    inverso=""
    for index in range(len(cadena) -1,-1,-1):
        inverso+=cadena[index]
    return inverso

"""def main():
    print("cadena",invert("Hola Undav!"))
main()"""
"""La forma mas simple"""

def invertircad(cadena):
    inverso=""
    for elem in cadena :
        inverso=elem+inverso
        #print(f"Debug: {inverso}")
    return inverso

"""def main():
    print("cadena inversa",invertircad("Hola Undav!") , " ,original: Hola Undav!")
main()"""