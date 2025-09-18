
def max_com_div(n,m):
    """
    Me dieron m y n 
    Busco el resto de la division entre m y n mientras r sea distinto de 0 
    pongo en m el valor de n m <--- n
    pongo en n el valor de r n <--- r
    busco el resto de la diviesion de m y n y la paso en r    r <-- m%n
    Cuando r sea igual a sero retorno n
    """
    r=m%n
    while r!=0:
        m=n
        n=r
        r=m%n
    return n


