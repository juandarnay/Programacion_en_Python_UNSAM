# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:04:27 2021

@author: Juan Augusto Darnay
"""

# fragmento de costo_camion.py
import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones*precio) de un archivo'''
    total = 0
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            fruta = row[0]
            ncajones = int(row[1])
            precio = float(row[2])
            lote = (fruta, ncajones, precio)
            camion.append(lote)
    return camion
