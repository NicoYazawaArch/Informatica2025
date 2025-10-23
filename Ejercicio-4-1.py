"""
 Definir (y documentar) dos funciones: …
a) una función denominada “es_par” que, dado un número entero por parámetro,
devuelva un valor booleano que indique si es par, o no. Dé ejemplos de invocación.
b) una función denominada “es_par_sn0” que, dado un número entero por parámetro,
devuelva como resultado “S” si es par, “N” si es impar o el carácter “0” si es cero.
c) Consulte la documentación mediante la función help ().
"""
def es_par(n):
    if n % 2==0:
        return True
    else:
        return False
    
def es_par_sn0(n):
    if n == 0:
        print("Es 0(cero).")
    elif n % 2==0:
        print("Es par.")
    else:
        print("Es impar.")

def main():
    f1=int(input("Ingrese numero entero: "))
    print(f"El valor es: {es_par(f1)}")
    f2=int(input("Ingrese numero entero: "))
    es_par_sn0(f2)
main()
