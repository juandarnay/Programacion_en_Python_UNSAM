## Código 2

# Ejercicio 1.18
# Autor: Mauro S. Ferraresi

cadenaO = input('Ingrese la palabra a convertir:')
cadenaGF1 = ''
cadenaGF2 = ''
"""
Usá una iteración sobre el string cadena para agregar la 
sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

Existen varias formas de realizar la conversion solicitada.

Forma 1 - Utilizacion de ciclo for e if como se solicita en el enunciado:


for c in cadenaO:
    if c.lower() == 'a': cadenaGF1 += c+'pa'
    elif c.lower() == 'e': cadenaGF1 += c+'pe'
    elif c.lower() == 'i': cadenaGF1 += c+'pi'
    elif c.lower() == 'o': cadenaGF1 += c+'po'
    elif c.lower() == 'u': cadenaGF1 += c+'pu'
    else: cadenaGF1 += c


print('Cadena original: ', cadenaO)
print('Cadena geringoso forma 1: ', cadenaGF1)
"""
"""
Forma 2 - Utilizacion del metodo replace como variante
"""
cadenaGF2 = cadenaO.replace('a','apa').replace('e','epe').replace('i','ipi').replace('o','opo').replace('u','upu').replace('A','APA').replace('E','EPE').replace('I','IPI').replace('O','OPO').replace('U','UPU')
print('Cadena geringoso forma 2: ', cadenaGF2)

