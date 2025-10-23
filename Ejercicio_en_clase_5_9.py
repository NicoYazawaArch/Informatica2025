"""
Problema para resolver
El hostal “La pulpería de Zoilo” es administrado por Alejo Omar Supiales, junto a su compañera y socia,
Estela Buroduro. El nombre del establecimiento fue heredado del negocio que en ese lugar, antiguamente,
atendía el abuelo de Alejo. Actualmente Estela se encarga de la parte administrativa y Alejo compone el
mantenimiento edilicio básico (plomería, electricidad, etc.). En Marzo, Junio, Septiembre y Diciembre, se
ajusta el tarifario, considerando variaciones estacionales de la demanda y el impacto de los aumentos en
costos de servicios y productos. En tiempos de escasez, comenta Estela, es necesario “afinar el lápiz” al
actualizar el tarifario de las 10 habitaciones, para lo cual hay que tener idea de la rentabilidad relativa de
cada tipo de hospedaje, de modo que es necesario un sistema informático que produzca información sobre
los niveles de ocupación de tres clases de habitaciones. Alejo describe que en la planta baja se ubican,
además de la “sala de estar” y el “desayunador”, tres habitaciones triples (31, 32 y 33), en el primer piso
cinco habitaciones dobles (101 a 105) y en el segundo piso dos habitaciones simples (201 y 202). En este
marco, proponen la realización de un sistema sencillo, donde los datos sean ingresados por un solo usuario,
sin necesidad de identificación ni contraseñas; algunos de los datos deberán ser controlados para asegurar
su validez, requiriendo el reingreso, en caso necesario, hasta que cumpla la condición válida. El propósito del
sistema es producir información, de detalle y estadística, de un determinado período estacional.
Respecto a los datos que el sistema debería solicitar al usuario, Estela afirma que el año (número entero de
2024 a 2034, incluidos) y el número de mes inicial (3, 6, 9 o 12), son datos imprescindibles para identificar el
período de la información, por lo cual debería controlarse su validez al momento de ingresarlos; ambos
datos son esenciales para controlar la validez de las fechas de estadía de huéspedes.
Respecto a las habitaciones ocupadas en el período, se espera que, por cada estadía, el usuario ingrese el
nro. DNI, el nombre y el apellido del huésped principal, también la “fecha de ingreso” (el día, el mes y el
año), el nro. de habitación asignada y la cantidad de días (entero mayor que cero y menor que 93). Se precisa
que el programa controle la validez de fechas (existente en el calendario y coherente con el período –la
fecha de ingreso debe pertenecer al período informado-), del nro. de habitación y de la cantidad de días.
Además, el programa debería mostrar en pantalla, junto a los datos válidos, DNI, nombre, apellido y fecha de
ingreso, el tipo de habitación (single, doble o triple) y la cantidad de días de estadía informados; se aclara
que cuando la estadía atraviesa dos períodos estacionales, los días de estadía se consideran solamente en el
período del ingreso (si el huésped ingresa el 31 de mayo y egresa el 10 de junio, se consideran 10 días de
estadía en el período marzo-mayo, sin computarlos en el período siguiente). Se destaca que si algún dato no
fuese válido, el programa debería solicitar su reingreso al usuario, hasta asegurar la validez antes de seguir.
Para las estadísticas, se espera que el programa determine y, finalmente, muestre en pantalla la cantidad de
estadías del período informadas y, por cada tipo de habitación (single, doble y triple), tanto la cantidad de
días de ocupación, como el nivel de uso (cantidad de días dividido cantidad de habitaciones del mismo tipo).
Se requiere a estudiantes de Informática de UNDAV, Especificar, Diseñar e Implementar en Python, un
programa (con todas sus funciones) que satisfaga el requerimiento precitado, respetando las condiciones de
presentación que se describen en la página siguiente.

El programa tiene que pedir al usuario ingresoo de legajo(int) y notas(int)
Repite ingreso en forma indefinida ingreso de notas hasta que el legajo es -1
Determinar nota maxima, nota minima, cantidad de notas y suma de notas y promedio 

Seudo codigo
Ingreso un legajo
notamax <- -1
notamin <- 11
suma <- 0
cont <- 0
mientras el legajo sea(int) distinto de -1 
    Ingreso nota
    Si la nota es mayor que notamax
        notamas <- nota



"""
def main():
