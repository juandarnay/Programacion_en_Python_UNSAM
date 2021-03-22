# rebotes.py
# Archivo de ejemplo
# Ejercicio

num_rebote = 1
metros = 100
salto = 0.6

while num_rebote <= 10:
    rebote = metros * salto
    print(num_rebote, round(rebote, 4))
    num_rebote = num_rebote + 1
    metros = rebote
