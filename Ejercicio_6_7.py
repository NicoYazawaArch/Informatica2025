"""
Ejercicio 6.7. Definir una función ‘oculta_digitos’ que, dada una cadena de caracteres como
parámetro, devuelva como resultado la cadena con todos sus dígitos reemplazados por el
carácter ‘*’. [Ej: para el argumento ‘su clave es: 1540’, debería devolver al programa
principal ‘su clave es: ****’ ]
"""

def ocultar_digitos(cadena):
    oculto=""
    digitos="0123456789" \
    ""
    for index in cadena:
        if index in digitos:
            oculto+="*"
        else:
            oculto+="*"
    return oculto

def main():
    clave=input("Ingrese clave: ")
    print(f"su clave es: {ocultar_digitos(clave)}")
main()