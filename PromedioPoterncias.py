def promedio_potencias(n,k):
    suma=0
    for i in range(1,n+1):
        potencia=i**k
        suma+=potencia
    promedio=suma/n
    return promedio

"""
def main():
    n1=int(input("ingrese primer numero: "))
    n2=int(input("Ingrese segundo numero: "))
    promedio=promedio_potencias(n1,n2)
    print("El promedio es: ", promedio)

main()
"""