"""
Definir una función denominada “es_bisiesto” que reciba por parámetro un
número, que representa un año, y devuelva un resultado booleano que indique si es, o no
es, bisiesto. Pruebe la función para múltiplos de 4, de 100 y de 400. [Nota: un año es
bisiesto si es un número divisible por 4, pero no es divisible por 100, excepto que
también sea divisible por 400. Ejemplos: 1984 y 2000 son bisiestos, 1800 no es bisiesto].
1- No es multiplo de 100 y es multiplo de 4.
2- Es multiplo de 100 y es multiplo de 400.O podriamos poner. -Es multiplo de 400

No es bisiesto si no se cumple lo de arriba. O sea, en todos los otros casos.

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0 :
        retorno=True
    else:
        retorno=False
    
    return retorno
main
if bisi: #No es necesarioo poner ==True ya que es booleano 
        print(f"{anio}. Es bisiesto")
    else:
        print(f"{anio}. No es bisiesto")    

"""

def es_bisiesto(anio):
    """
    Recibe un anio (int) como parametro
    Retorna True si anio es bisiesto. False si anio no es bisiesto
    """
    """
    Segun el razonamiento de arriba
    Un año es bisiesto cuando no es multiploo de 100 y es multiplo de 4 0 es multiplo de 400
    Esta expresion da True cuando el año es bisiesto y False cuando el año no lo es.
    Puedi retornar directamente el resultado de esta exprecion.
    """
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0
"""
def main():
    anio=int(input("Ingrese año: "))
    #bisi=es_bisiesto(anio) se puede poner directo en el if ya que solo lo va a evaluar
    if es_bisiesto(anio): #No es necesarioo poner ==True ya que es booleano  
        print(f"{anio}. Es bisiesto")
    else:
        print(f"{anio}. No es bisiesto")    
main()
"""