"""
Ejercicio 7.11. Definir dos funciones. Una función con dos parámetros, una lista de enteros
y un entero k,…
a) que devuelva como resultado otra lista que incluya sólo los que sean múltiplos de k .
b) que devuelva como resultado otra lista compuesta por tres listas: la primera con los
mayores a k, la segunda con los iguales a k y la tercera con los menores.
"""
def multiplos_k(lista,k):
    multiplos=[]
    for i in lista:
        if i%k == 0 :
            multiplos.append(i)
    return multiplos

def comparacion(lista,k):
    listacompuesta=[]
    listmayores=[]
    listmenores=[]
    listiguales=[]
    for i in lista:
        if i > k :
            listmayores.append(i)

        elif i == k :
            listiguales.append(i)

        else:
            listmenores.append(i)

    listacompuesta.append(listmayores)
    listacompuesta.append(listiguales)
    listacompuesta.append(listmenores)
    return listacompuesta


def main():
    lista1 = [1, 5, 10, 0, 20, 5, -4]
    k1 = 5
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 2
    print(f"Multiplos de k= {k} en {lista} : Resultado {multiplos_k(lista,k)}")
    print(f"Lista de menores iguales y mayores de k= {k1} en {lista1} : Resultado {comparacion(lista1,k1)}")
main()