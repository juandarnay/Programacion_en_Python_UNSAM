# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:37:06 2021

@author: Juan Augusto Darnay
"""

# Ejercicio 2.2: Lectura de un archivo de datos

# Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple con los datos leídos.

# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

# Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo como punto flotante, usá float(s).

# Tu programa debería imprimir una salida como la siguiente:

# Costo total 47671.15

import os

with open 