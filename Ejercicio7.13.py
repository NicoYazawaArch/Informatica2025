"""
Ejercicio 7.13. Definir una función que reciba como parámetro una lista de tuplas, cada una
de la forma (apellido, nombre, inicial_segundo_nombre), y devuelva como resultado una lista
de cadenas de caracteres, cada una de las cuales contenga primero el nombre, un espacio,
luego la inicial con un punto, un espacio y luego el apellido.
"""
def nombres(lista):
    listacad=[]
    for apellido,nombre,inicial in lista:
        cadena= nombre, inicial , apellido
        listacad.append(cadena)

    return listacad
    

def main():
    lista_de_tuplas = [
    ("Garcia", "Juan", "C"),
    ("Martinez", "Ana", "M"),
    ("Perez", "Luis", "J")
    ]
    print(f"Lista orginal  {lista_de_tuplas}")
    print(f"Nombres organizados {nombres(lista_de_tuplas)}")
main()