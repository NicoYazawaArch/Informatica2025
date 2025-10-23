"""
Ejercicio 6.12. Definir (y documentar) una función ‘inicial_mayuscula’ que, dada por
parámetro una cadena de caracteres, devuelva como resultado dicha cadena con la
primera letra de cada palabra en mayúsculas. [Ej: para el argumento ’república
argentina’ debería devolver al programa principal ’República Argentina’ ].
Utilice la función ord(…), que devuelve el número ordinal de un carácter, y la función
chr(…), que devuelve el carácter correspondiente a un ordinal del rango [0,256].
Ejemplos: ord (‘a’) es 97 y chr (65) es ‘A’.

La diferencia entre una minúscula y su mayúscula es siempre 32 (ej: 97 - 65 = 32).
inicial_mayuscula(cadena):
resultado <-- " " 
bandera<-- True
inicio_minusculas <-- 97 (ord("a"))
fin_minuscula<-- 122 (ord("z"))
conversion<-- 32 (Defirencia entre "a" y "A")

Para cada caracter en cadena
Si caracter=="":
    resultado<-- resultado + " "
    bandera= True

Si no es bandera es True y ord(caracter)>= Inicio_minuscula y ord(caracter)<= fin_minuscula
        numerico<--ord(caracter)
        convertido<--numerico - conversion
        resultado<--resultado + chr(convertido)

        bandera<--False
Si no:
    resultado<-- resultado + caracter
    bandera<--False

retornar resultado


"""
def inicial_mayuscula(cadena):
    resultado=""
    bandera=True

    mayuscula=32
    inicio_minuscula=97
    fin_minusculas=122

    for caracter in cadena:
        valor_ord=ord(caracter)
        if caracter==" ":
            resultado+=" "
            bandera=True
        elif bandera and (valor_ord >= inicio_minuscula and valor_ord <= fin_minusculas):
            numerico=valor_ord - mayuscula
            resultado+=chr(numerico)
            bandera=False
        else:
            resultado+= caracter
            bandera=False
    return resultado

def main():
    ejemplo1 = "república argentina"
    print(f"Original: '{ejemplo1}'")
    print(f"Convertida: '{inicial_mayuscula(ejemplo1)}'")

main()
