"""
Ejercicio 7.14. Definir dos funciones. Una función que reciba como parámetro una lista,…
a) y devuelva como resultado una nueva lista con los mismos elementos, pero en orden
invertido. (Ej: para el argumento [‘Di’, ‘buen’, ‘dia’, ‘a’, ‘papi’], debería devolver al
programa principal [‘papi’, ‘a’, ‘dia’, ‘buen’, ‘Di’], sin modificar la lista original.)
b) que la invierta (sin usar listas auxiliares) y la devuelva modificada al programa
principal. ¿Es necesaria la instrucción return en la función?
"""
def inversor(lista):
    invertida=[]
    for cadena in lista:  #este tambien es valido 
        invertida.insert(0,cadena)    
    return invertida


def main():
    cadena= ['Di', 'buen', 'dia', 'a', 'papi']
    print(f"lista cadena a invertir {cadena} \nCadena invertida {inversor(cadena)} ")
#main()


#En clase parece que esta version la cadena entra en lista
def invertir_lista_a(lis):
    lis_invertida=[]
    #l=len(lis)
    for i in range(-1,-len(lis)-1,-1):
        lis_invertida.append(lis[i])
    return lis_invertida

def main1():
    l=["Di","buen","dia","a","papi"]
    li= invertir_lista_a(l)
    print(li)

#main1()

#con laa lista pero con insert
def invertir_lista_a1(lis):
    lis_invertida=[]
    #l=len(lis)
    for i in range(len(lis)):
        lis_invertida.insert(0,lis[i])
    return lis_invertida

def main2():
    l=["Di","buen","dia","a","papi"]
    print(l)
    li= invertir_lista_a(l)
    print(li)
#main2()

#punto b)

def invertir_lista_sin_auxi(lis):
    for i in range (len(lis)//2):
        auxi=lis[-i-1]
        lis[-i-1]=lis[i]
        lis[i]=auxi
    return lis

def mainB():
    l=["Di","buen","dia","a","papi"]
    print(l)
    li= invertir_lista_sin_auxi(l)
    print(li)
#mainB()


#Con Tupla
def invertir_tupla(tup):
    for i in range (len(tup)//2):
        auxi=tup[-i-1]
        tup=tup[:-i-1]+(tup[i],)+tup[-i:]
        tup=tup[:i]+(auxi,)+tup[i+1:]
    return tup
#se estaria duplicando para difirencial la mutabilidad de las listras


def mainT():
    t=("Di","buen","dia","a","papi")
    print(t)
    li= invertir_tupla(t)
    print(li)
mainT()

#version con un return
def invertir_crear_nueva(lista_original):
    """
    Recibe una lista y devuelve una NUEVA lista con los mismos
    elementos, pero en orden invertido. La lista original no se modifica.

    Args:
        lista_original (list): La lista que se usará como base.

    Returns:
        list: Una nueva lista invertida.
    """
    # La forma más simple en Python de obtener una copia invertida
    # es usando 'slicing' (rebanado) con un paso de -1.
    # Esto crea una lista completamente nueva en memoria.
    return lista_original[::-1]