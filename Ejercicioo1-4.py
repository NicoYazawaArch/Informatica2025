"""Exprese la situciaones enunciadas asgnacion y salidas en pantalla Utilize unicamente variable cuyo identificadores son dinero, paraguas, precio_unitario, cant_parag_venta"""
def main():
    """Este progrma pide al usurio que ingrese la cantidad de dinero inicial, paraguas inniciales y el pprecio y luego imprime los valores"""
    #Esta es la parte que se ingresan todos los datos
    dinero=float(input("Ingrese la cantidad inicial de dinero: "))
    paraguas=int(input("Ingrese la cantidad inicial de paraguas: "))
    precio_unitario=float(input("Ingrese el precio unitario: "))
   
    #punto b
    cant_parag_ventas=paraguas//5
    paraguas -=cant_parag_ventas
    dinero+=cant_parag_ventas+precio_unitario
    #Punto c
    cant_parag_ventas=paraguas//3
    paraguas-=cant_parag_ventas
    dinero+=cant_parag_ventas*precio_unitario

    #Esta es la parte que se imprimen todos los valores
    print("Ingrese cantidad inicial de dinero",dinero)
    print(f"Inicialmente tenemos {paraguas} paraguas")
    print(f"precio unitario {precio_unitario}")

    print(f"Paraguas vendidos: {cant_parag_ventas}")
    print(f"Paraguas restantes: {paraguas}")
    print(f"Dinero en caja actualizado: ${dinero:.2f}")
main()
