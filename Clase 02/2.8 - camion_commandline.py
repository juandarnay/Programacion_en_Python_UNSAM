'''
Copiá el contenido de costo_camion.py a un
nuevo archivo llamado camion_commandline.py
que incorpore la lectura de parámetros por
línea de comando según la sugerencia del
siguiente ejemplo:
'''
# camion_commandline.py
import csv
import sys


def costo_camion(nombre_archivo):
    total_cajones = 0
    costo_frutas = 0
    costo_total = 0

    f = open (nombre_archivo, "rt")
    encabezados = next(f).split(",")
    for linea in f:
        try:
            fila = linea.split(",")
            fruta = fila[0]
            cajones = int(fila[1])
            costo_unitario_frutas = float(fila[2])
            total_cajones += cajones
            costo_frutas += costo_unitario_frutas
            costo_total += (cajones * costo_unitario_frutas)
        except ValueError:
            print("Te faltó alguna cosa belleza")
    return costo_total
    f.close()

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = r'D:\Dropbox\Ciencia de datos\Programacion en Python UNSAM\Notas\01_ejercicios_python\Data\camion.csv'
