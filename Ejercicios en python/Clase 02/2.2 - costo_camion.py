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

total_cajones = 0
total_costo_unitario_fruta = 0
costo_total = 0

f = open ('C:\\Dropbox\\Ciencia de datos\\Programacion en Python UNSAM\\Notas\\01_ejercicios_python\\Data\camion.csv', "rt") 
encabezados = next(f).split(",")
for linea in f:
    fila = linea.split(",")
    print(fila)
    fruta = fila[0]
    cajones = int(fila[1])
    costo_fruta = float(fila[2])
    total_cajones += cajones
    total_costo_unitario_fruta += costo_fruta
    costo_total += (cajones * costo_fruta)
    
    
print("el total de cajones es:", total_cajones)
print("el costo total unitario de la fruta es:", round(total_costo_unitario_fruta, 2))
print("Costo total:", round(costo_total, 2))
f.close()