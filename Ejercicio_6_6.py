"""
Ejercicio 6.6. Definir una función “sustituye_chr” que, dados como parámetros una cadena
de caracteres txt y dos caracteres c1 y c2, devuelva como resultado una cadena con la
sustitución, en txt, de todos los caracteres iguales a c1 , por el carácter c 2. [Ej: pasados
como argumentos el texto ‘mi primer modulo.py’, el carácter ‘ ‘ y el carácter ‘_‘, debería
devolver al programa principal ‘mi_primer_modulo.py’ ]
"""
def sustituye_chr(cadena,c1,c2):
    txt=""
    for c in cadena:
        if c==c1:
            txt+=c2
        else:
            txt+=c
    return txt

def main():
    print("Original : mi primer modulo.py ",sustituye_chr('mi primer modulo.py', ' ', '_'))
main()  