"""
Escribir una función que reciba 3 enteros como parámetros (n1, n2 y n3). 
La función deberá tomar uno por uno los enteros del rango n1 a n2 (extremos incluidos) y elevarlos a n3. 
La función deberá retornar el promedio de todas las potencias.

Ej.:

Si n1=3, n2=7 y n3=3

La función deberá hacer (27 + 64 + 125 + 216 + 343)  / 5 = 775 / 5 = 155

"""
def calculo(n1,n2,n3):
    cuenta=0
    cant_numeros=0
    for i in range(n1,n2+1):
        cant_numeros+=1
        cuenta+= i**n3
    promedio=cuenta/cant_numeros
    return promedio 

def main():
    n1=3
    n2=7
    n3=3
    print("EL caluculo es: ", calculo(n1,n2,n3))
main()