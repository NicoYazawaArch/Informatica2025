"""

Ejercicio 7.9. Definir dos funciones. Una función denominada…
a) ‘interseccion’ que reciba por parámetro dos listas, que representan conjuntos, y
devuelva como resultado otra lista que incluya, sin repeticiones, los elementos
comunes a ambas listas pasadas como argumentos.
b) ‘union’ que reciba por parámetro dos listas, que representan conjuntos, y devuelva
como resultado otra lista que incluya, sin repeticiones, los elementos que
pertenezcan a una u otra lista pasadas como argumentos.

"""
#a
def interseccion(lista1,lista2):
    listacomun=[]
    for elem in lista1:
        if elem in lista2 and elem not in listacomun:
            listacomun.append(elem)
    return listacomun

def union(lista1,lista2):
    listacombinada=lista1+lista2
    listafinal=[]
    for elem in listacombinada:
        if elem not in listafinal:
            listafinal.append(elem) 

    return listafinal

def main():
    conjunto_A = [1, 2, 2, 3, 4, 5]
    conjunto_B = [4, 5, 5, 6, 7]
    print("Interseccion entre listas: ", interseccion(conjunto_A,conjunto_B))
    print("union de listas: ", union(conjunto_A,conjunto_B))
main()