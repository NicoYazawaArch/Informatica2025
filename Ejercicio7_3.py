"""
Ejercicio 7.3. Definir una función ‘encaja_domino’, que reciba por parámetro dos tuplas que
representan fichas de dominó y devuelva un resultado booleano que indique si encajan o no.
[Ej: las fichas (3, 4) y (4, 1) encajan, porque coinciden en el número 4. Ídem (4, 4) y (5, 4) ]
"""
def encaja_domino(ficha1,ficha2):
    bandera=None
    if ficha1[0] in ficha2 or ficha1[1] in ficha2:
        bandera=True
    else:
        bandera=False
    return bandera

def main():
    ficha_a = (3, 4)
    ficha_b = (4, 1) # Encajan (por el 4)
    
    ficha_c = (4, 4)
    ficha_d = (5, 4) # Encajan (por el 4)
    
    # Ejemplo que no encaja
    ficha_e = (1, 2)
    ficha_f = (5, 6) # No encajan
    
    ficha_g = (4, 4)
    ficha_h = (5, 6) # No encajan

    print(f"¿(3, 4) y (4, 1) encajan? R: {encaja_domino(ficha_a, ficha_b)}")
    print(f"¿(4, 4) y (5, 4) encajan? R: {encaja_domino(ficha_c, ficha_d)}")
    print(f"¿(1, 2) y (5, 6) encajan? R: {encaja_domino(ficha_e, ficha_f)}")
    print(f"¿(4, 4) y (5, 6) encajan? R: {encaja_domino(ficha_g, ficha_h)}")
main()