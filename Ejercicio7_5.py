"""
Ejercicio 7.5. Definir una función ‘es_tupla_ordenada’, que reciba como parámetro una
tupla de elementos y devuelva un resultado booleano que indique si se encuentran
ordenados de menor a mayor.
"""

def es_tupla_ordenada(tup):
    bandera=True
    for i in range(len(tup)-1):
        if tup[i]>tup[i+1]:
            bandera= False
    return bandera

def main():
    tupla_1 = (1, 2, 3, 4, 5)
    tupla_2 = (1, 3, 2, 5) # Desordenada en 3 > 2
    tupla_3 = ("a", "b", "c")
    tupla_4 = ("z", "a")
    tupla_5 = (10, 10, 12, 15) # Ordenada (permite elementos iguales)
    tupla_6 = (5,) # Ordenada (un solo elemento)
    tupla_7 = () # Ordenada (vacía)

    print(f"{tupla_1} -> {es_tupla_ordenada(tupla_1)}")
    print(f"{tupla_2} -> {es_tupla_ordenada(tupla_2)}")
    print(f"{tupla_3} -> {es_tupla_ordenada(tupla_3)}")
    print(f"{tupla_4} -> {es_tupla_ordenada(tupla_4)}")
    print(f"{tupla_5} -> {es_tupla_ordenada(tupla_5)}")
    print(f"{tupla_6} -> {es_tupla_ordenada(tupla_6)}")
    print(f"{tupla_7} -> {es_tupla_ordenada(tupla_7)}")
main()