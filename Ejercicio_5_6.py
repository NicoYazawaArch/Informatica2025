"""
Ejercicio 5.6. Definir y documentar una función “es_potencia_de_dos” que reciba como
parámetro un número natural, y devuelva el valor booleano True si el número es una
potencia de 2, y False en caso contrario.

El número 8 es una potencia de 2. 8÷2=4, 4÷2=2, 2÷2=1. El proceso termina en 1.

El número 6 no es una potencia de 2. 6÷2=3. Como 3 no es par, no se puede seguir dividiendo por 2.

"""

def es_potencia_de_dos(n):
    if n<=0:
        return False
    while n%2==0:
        n=n/2
    return n==1 #Si n es 1, retorna True. Si no, retorna False.
def main():
    print(f"¿Es 8 una potencia de 2? {es_potencia_de_dos(8)}")
    print(f"¿Es 16 una potencia de 2? {es_potencia_de_dos(16)}")
    print(f"¿Es 1 una potencia de 2? {es_potencia_de_dos(1)}")
    print(f"¿Es 12 una potencia de 2? {es_potencia_de_dos(12)}")
    print(f"¿Es 0 una potencia de 2? {es_potencia_de_dos(0)}")
main()