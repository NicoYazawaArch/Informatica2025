"""
Ejercicio 5.4. Definir una función “max_com_div” que, dados por parámetro dos números n
y m, devuelva como resultado el Máximo Común Divisor entre ambos, implementando el
algoritmo de Euclides. Se describen a continuación los pasos de ese algoritmo matemático:
1. Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
2. Si r es cero, entonces n es el MCD de los valores iniciales.
3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.


1-Divide el número mayor por el menor:
48÷18=2 con un resto de 12. (El resto, r, es 12).
m=48,n=18.

2-Si el resto es 0, el segundo número es el MCD. Si no, repite con nuevos números:
Como 12 / 0, continuamos.

3-El divisor (18) se convierte en el nuevo número mayor, y el resto (12) se convierte en el nuevo número menor:
Ahora, la división es 18÷12=1 con un resto de 6.
m=18,n=12.

4-Repite hasta que el resto sea 0:
Como 6 no es igual 0, continuamos.
Ahora, la división es 12÷6=2 con un resto de 0.
m=12,n=6.

5-El resto es 0, el divisor es el MCD:
Como el resto es 0, el último divisor utilizado, que es 6, es el Máximo Común Divisor de 48 y 18.

"""

def max_com_div(n,m):
    if n>m:
        n,m = m,n #Intercambia lugar de los valores 
    while n != 0:
        #Se obtiene el resto de la división entera.
        r=m%n
        #Se reemplaza m por n y n por r.
        m=n
        n=r
        #Cuando el bucle termina porque el resto es 0 , m contiene el MCD
    return m

def main():
    n1=int(input("Ingrese primer numero: "))
    n2=int(input("Ingrese segundo numero: "))
    print(f"EL MCD entre {n1} y {n2} es: {max_com_div(n1,n2)}")
main()