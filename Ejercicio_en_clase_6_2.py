'''
Ejercicio 6.2. Definir una función “segm_3_txt” que, dados como parámetros una cadena de caracteres y un carácter (que denominaremos selector):

a) Imprima los tres primeros caracteres de la cadena, si el valor del selector es la letra ‘P’, o los tres últimos caracteres si el valor del selector es ‘U’, o el mensaje
‘Error en el selector’ si el valor del selector no es ‘P’ ni ‘U’.
'''
def segm_3_txt (cadena, selector):
    if selector in 'P' or "p":
        print(cadena[:3])
    elif selector in 'U' or "u":
        print(cadena[-3:])
    else:
        print("[DEBUG---Error en selector]")