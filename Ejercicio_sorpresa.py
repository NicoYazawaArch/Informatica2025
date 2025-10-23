"""
a-	Escribir una función que reciba, como parámetros, tres números NATURALES (enteros positivos): m, n,  r. 
La función deberá revisar todos los valores entre m y n (AMBOS INCLUIDOS) y CONTAR la cantidad de múltiplos de r.
La función deberá retornar el resultado de esa cuenta. NOTA: el primer número puede ser mayor, menor o igual al segundo.
b-	Escribir otra función que reciba, como parámetros,  cuatro números NATURALES: m, n, r,  s. 
Deberá recorrer todos los valores en el intervalo r, s (AMBOS INCLUIDOS). 
Para cada uno de esos valores, usando la función anterior, deberá contabilizar la cantidad de múltiplos en el intervalo m, n y conservar la cantidad máxima de múltiplos. 
La función deberá retornar la cantidad máxima de múltiplos relevada.
"""

"""
Si m es mayor a n
    intercambio m y n
recorrer con i el intervalo entre m y n (incluidos ambos)
    si i es multiplo de r
        lo cuento en el contador
retorno el valoor del contador
"""
def numeros_naturales(m,n,r):
    cont_multiplos=0
    if m>n:
        m,n=n,m

    for i in range(m,n+1):
        if i % r == 0:
            cont_multiplos+=1

    return cont_multiplos

def main():
    m=int(input("Ingrese el numero m: "))
    n=int(input("Ingrese el numero n: "))
    r=int(input("Ingrese el numero r: "))
    print(f"El numero multiplo: {numeros_naturales(m,n,r)}")
main()
