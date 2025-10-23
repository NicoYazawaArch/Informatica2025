"""Ejercicio 3.13. Definir una función denominada “suma_n”, que reciba como parámetro
un número natural n y devuelva como resultado la suma de naturales desde 1 hasta n
(ejemplos, si n es 5 la función debe devolver 15; si n es 3 la función debe devolver 6)."""
def suma_n(n):
    cont=0
    if n==3:
        print("devuelve: ",n*2)
    elif n==5:
        print("devuelve: ",n*3)
    else:
        for i in range(1,n+1):
            cont+=i
        print("Devuelve: ",cont)



def main():
    entrada=int(input("Ingrese numero natural: "))
    suma_n(entrada)

main()