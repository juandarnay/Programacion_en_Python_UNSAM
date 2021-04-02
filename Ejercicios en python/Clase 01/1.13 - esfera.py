# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:40:25 2021

@author: Juan Augusto Darnay
"""
# Ejercicio 1.13: El volúmen de una esfera

# En tu directorio de trabajo, escribí un programa llamado esfera.py que le pida al usuario que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

# Finalmente, ejecutá el programa desde la línea de comandos para responder ¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.

pi = 3.141592653589793

radio = int(input("hola, ¿de qué radio te gustaría tu esfera?"))
volumen = (4/3) * pi * radio**3

print(volumen)



