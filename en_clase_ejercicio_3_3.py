#ejercicio 3.3
#a)
def hms_a_segtot(horas,minutos,segundos):
    """
    Recibbe como parametros:
        horas(int): representa un valor de horas
        minutos(int): representa un valor de minutos 
        segundos(int): representa un valor de segundos
    hms_a_segtot calcula la cantidad de segundos que equivale el tiempo recivido y retorna:
        seg_tot(int): La cantidad de segundos equivalente al tiempo recibido.
            Ejemplo:
            Si reciboo hora=2, minutos=5, segundos=30 --> retorna:
            2 horas --> 2 * 33600 = 7200 segundos
            5 minutos --> 5 * 60 = 300 segundos
            30 segundos --> 30 segundos
            Tiempo total a retornar 7530 seg
        """
    seg_horas=horas*3600 #Segundos en horas
    seg_minutos=minutos*60 #Segundos en minutos
    seg_tot=seg_horas+seg_minutos+segundos
    #print(f"debug: --> {seg_tot}")
    
    return seg_tot

#b)
def segtot_a_hms(seg_tot):
    horas= seg_tot//3600
    segundos_sobrantes=seg_tot%3600
    minutos=segundos_sobrantes//60
    segundos=segundos_sobrantes%60
    return horas , minutos , segundos


"""

def main():
    h=int(int(input("Ingrese el numero de horas: ")))
    m=int(int(input("Ingrese el numero de minutos ")))
    s=int(int(input("Ingrese el numero de segundos: ")))

    st=hms_a_segtot(h,m,s)
    
    print("Los segundos totales son: ",st)

    h1,m1,s1=segtot_a_hms(st)

    print(f"{h1} horas {m1} minutos {s1} segundos")

main()

"""

