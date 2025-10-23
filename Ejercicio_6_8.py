"""
Ejercicio 6.8. Definir una función ‘separa_miles’ que, dada por parámetro una cadena de
caracteres que contiene un largo número entero, devuelva como resultado la cadena con las
separaciones de miles incluidas en el número. [Ej: para el argumento ‘1234567890’ debería
devolver al programa principal ‘1.234.567.890’ ]
"""
def separa_miles(cadena):
    separado=""
    contador=0
    for index in range(len(cadena)-1,-1,-1):
        contador+=1
        actual=cadena[index]
        separado=actual+separado
        if contador%3==0 and index!=0:
            separado="."+separado

    return separado

def main():
    print("1234567890 debe devolver, 1.234.567.890 ejecucion:", separa_miles("1234567890"))
main()