def  es_potencia_de_dos(n):
    if n <1 :
        return False
    while n%2==0:
        n=n//2
    if n==1:
        salida=True
    else :
        salida=False
    return salida


def main():
    for i in range (0,21):
        print(f"Es potencia, {i} ,{es_potencia_de_dos(i)}")
main()