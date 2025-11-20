"""
Ejercicio 7.4. Definir una función ‘producto_escalar’, que reciba como parámetros dos
tuplas, que representan vectores de igual dimensión, y devuelva como resultado el valor de
su producto escalar.{El producto escalar de los vectores (u1, u2, u3) y (v1, v2, v3), se puede
calcular como el valor numérico que resulta de sumar los productos de las componentes
homólogas: u1 * v1 + u2 * v2 + u3 * v3. Ej.: si recibe (5,1,0,3) y (2,4,9,3) debe devolver 23 }
"""

def producto_escalar(vector1,vector2):
    productoTotal=0
    dimencion=len(vector1)
    for i in range(dimencion):
        u=vector1[i]
        v=vector2[i]
        productoTotal+=(u*v)

    return productoTotal

def main():
    v1 = (5, 1, 0, 3)
    v2 = (2, 4, 9, 3)
    print(f"El producto escalar de {v1} entre {v2} es {producto_escalar(v1,v2)}")

main()
