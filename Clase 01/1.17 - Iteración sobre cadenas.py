cadena = "Ejemplo con for"

num_letras = 0

for i in cadena:
    if "o" in i:
        num_letras = num_letras + 1
    else: num_letras = num_letras + 0
print(num_letras)

'''
Alternativa

for i in cadena:
    if i == "o":
        num_letras = num_letras + 1
    else: num_letras = num_letras + 0
print(num_letras)
'''
