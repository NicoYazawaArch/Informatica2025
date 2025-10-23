"""
Escribir una función que reciba 3 enteros como parámetros (n1, n2 y n3). La función deberá tomar uno por uno los enteros del rango n1 a n2 (extremos incluidos) y elevarlos a n3. La función deberá retornar el promedio de todas las potencias.

Ej.:

Si n1=3, n2=7 y n3=3

La función deberá hacer (27 + 64 + 125 + 216 + 343)  / 5 = 775 / 5 = 155

Inicializo acum en 0
inicializo cont en 0
recorro con u el intervalo n1(incluido , n2 (incluido)
    sumo al acumulador la potencia i a la n3
    simo 1 añ contador
si contador es distito de 0
    promedio <- acumulador/contador
si no 
    promedio =0
retorno promedio


"""
def prom_pot(n1,n2,n3):
    acum=0
    cont=0
    for i in range(n1,n2+1):
        acum+=i**n3
        cont+=1
    if cont != 0:
        prom= acum/cont
    else:
        prom=0
    return prom

def main():
    n1=int(input("Ingrsde el numero inicio: "))
    n2=int(input("Ingrese el numero final: "))
    n3=int(input("Ingrese la potencia: "))
    print("Resultado de : ", prom_pot(n1,n2,n3))


main()