"""
Ejercicio 7.12. Definir una función ‘lista_de_minimos’ que, dadas por parámetro dos listas
de igual longitud, compuestas por números, devuelva como resultado una nueva lista que
contenga en cada posición el menor entre los elementos correspondientes de ambas listas.
"""
def lista_de_minimos(lista1,lista2):
    compuesta=[]
    long=len(lista1)
    for i in range(long):
        if lista1[i]<lista2[i]:
            compuesta.append(lista1[i])
        else:
            compuesta.append(lista2[i])
    return compuesta

def main():
    l1 = [1, 5, 10, 30]
    l2 = [3, 2, 12, 25]
    print(f"Los minimos entre Lista 1 {l1} y Lista 2 {l2} :  \nLista de minimos = {lista_de_minimos(l1,l2)}")
main()