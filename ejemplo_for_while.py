def prod_en_sumas_for(num,cant):
    """Calcula el producto de dos numeros por sumas sucesivas"""
    prod=0
    for i in range(cant):
        prod=prod+num
    return prod

def prod_en_sumas_while(num,cant):
    """Calcula el producto de los dos numeros por sumas sucesivas usando ciclos indefinidos"""
    prod=0
    contador=0
    while contador<cant:
        prod=prod+num
        print(f"--[Debug]El resulltado del parcial es: {prod} {contador}")
        contador=contador+1
    return prod

def main():
    print(f"for: {prod_en_sumas_for(5,3)}")
    print(f"while: {prod_en_sumas_while(5,3)}")


main()