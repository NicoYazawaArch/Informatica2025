"""b) Dado un número natural n, imprimir la suma total de los naturales de 1 a n."""
def sumatoria():
    n = int(input("Introduce un número natural para calcular la suma: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
        # Imprimimos el resultado final
    print(f"La suma de los números naturales desde 1 hasta {n} es: {suma}")

sumatoria()
