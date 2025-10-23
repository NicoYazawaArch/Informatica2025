"""a) Dado un número natural n, imprimir su tabla de multiplicar desde 0 hasta n."""
def multiplicador():
    n = int(input("Introduce un número natural para la tabla de multiplicar: "))
    
    print(f"Tabla de multiplicar del {n}")
    
    for i in range(n + 1):
        resultado = n * i
    print(f"{n} x {i} = {resultado}")

multiplicador()
