'''
jercicio 1.18: Geringoso rústico

Usá una iteración sobre el string cadena para agregar la sílaba 'pa',
'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

'''

cadena = 'Geringoso'

capadepenapa = ''

for letras in cadena:
    if letras in "a":
            capadepenapa = capadepenapa + "apa"
            print(capadepenapa)
    elif letras in "e":
            capadepenapa = capadepenapa + "epe"
            print(capadepenapa)
    elif letras in "i":
            capadepenapa = capadepenapa + "ipi"
            print(capadepenapa)
    elif letras in "o":
            capadepenapa = capadepenapa + "opo"
            print(capadepenapa)
    elif letras in "u":
            capadepenapa = capadepenapa + "upu"
            print(capadepenapa)
    else:
            capadepenapa = capadepenapa + letras

print(capadepenapa) 


'''
cadena = 'geringoso'
for letra in cadena:
    if letra in 'aeiou':
        cadena += letra + 'p' + letra
    else:
        cadena += letra
print(cadena)

'''
