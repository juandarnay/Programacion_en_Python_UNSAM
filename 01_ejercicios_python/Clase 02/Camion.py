# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:40:57 2021

@author: Juan Augusto Darnay
"""
import os
os.getcwd()

with open("C:\Dropbox\\Ciencia de datos\\Programacion en Python UNSAM\\Notas\\01_ejercicios_python\\Data\camion.csv", "rt", encoding='utf8') as f:
    for linea in f:
        print(linea, end = "")

f = open("C:\Dropbox\\Ciencia de datos\\Programacion en Python UNSAM\\Notas\\01_ejercicios_python\\Data\camion.csv", "rt", encoding='utf8')

f = open("C:\\Dropbox\\Ciencia de datos\\Programacion en Python UNSAM\\Notas\\01_ejercicios_python\\Data\\camion.csv", "rt")
headers = next(f).split(',')
headers
