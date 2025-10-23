"""
Ejercicio 6.9. Definir una función que, dadas dos cadenas de caracteres como parámetros,
devuelva como resultado la cadena que sea anterior en orden alfabético. [Ej: para los
argumentos ‘kde’ y ‘gnome’ debería devolver al programa principal ‘gnome’ ]

"""

def pba (cad1,cad2):

    if cad1 < cad2:
        return cad1
    else:
        return cad2
    
def main():
    print("Devuelve: ", pba("kde","gnome"))

main()
    
