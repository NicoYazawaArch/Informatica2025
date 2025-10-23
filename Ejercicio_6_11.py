"""
Ejercicio 6.11. Definir una función ‘letras_iniciales’ que, dada por parámetro una
cadena de caracteres, devuelva como resultado una cadena con las primeras letras de
cada palabra. [Ej: para el argumento ‘Universal Serial Bus’ debería devolver al
programa principal ‘USB’ ]
"""

def letras_iniciales(cadena):
    iniciales=""
    inicio=True
    for caracter in cadena:
        if caracter==" ":
            inicio=True
        elif inicio:
            iniciales+=caracter
            inicio=False
    return iniciales

def main():
    ejemplo1 = "Universal Serial Bus"
    print(f"'{ejemplo1}' -> '{letras_iniciales(ejemplo1)}'") # Salida: USB
    
    ejemplo2 = "Hyper Text Markup Language"
    print(f"'{ejemplo2}' -> '{letras_iniciales(ejemplo2)}'") # Salida: HTML
    
    ejemplo3 = "  hola mundo " # Con espacios extra
    print(f"'{ejemplo3}' -> '{letras_iniciales(ejemplo3)}'") # Salida: hm

main()