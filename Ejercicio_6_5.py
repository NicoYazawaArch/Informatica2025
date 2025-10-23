"""
Ejercicio 6.5. Definir una función “intercala_chr” que, dados como parámetros una cadena
de caracteres y un carácter, devuelva como resultado la cadena con el carácter insertado
entre sus caracteres originales. [Ej: para los argumentos ‘veamos’ y ‘-‘, debería devolver al
programa principal ‘v-e-a-m-o-s’ ]
"""
def intercala_chr(cadena,caracter):
    guardados=""
    for elem in cadena:
        guardados+=elem+caracter
        print(f"Debug: {guardados}")
    return guardados[:-1]

def main():
    print("Veamos con ' - ' ---> ",{intercala_chr("Veamos","-")})
main()