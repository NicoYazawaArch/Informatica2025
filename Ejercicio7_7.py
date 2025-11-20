"""
Ejercicio 7.7. Definir una función ‘suma_vectores’ que, dadas por parámetro dos tuplas
que representan vectores de igual dimensión, devuelva como resultado una lista que
represente su suma vectorial. {La suma de vectores ( u1, u2, u3 ) y ( v1, v2, v3 ), se
calcula como el vector que resulta de sumar las componentes homólogas de ambos:
(u1 + v1 , u2 + v2 , u3 + v3). Ej: si recibe (5,1,0,3) y (2,4,9,3) debe devolver [7,5,9,6] }
"""
def suma_vectores(vector1,vector2):
    dimencion=len(vector1)
    lista=[]
    for i in range(dimencion):
        sumavector=vector1[i]+vector2[i]
        lista.append(sumavector)
    return lista

def main():
    u=(5,1,0,3)
    v=(2,4,9,3)
    print(f"la suma del vectores u+v : {u} + {v} = {suma_vectores(u,v)} ")
main()