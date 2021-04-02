import csv
f = open(r'C:\Dropbox\Ciencia de datos\Programacion en Python UNSAM\Notas\01_ejercicios_python\Data\camion.csv')
rows = csv.reader(f)
headers = next(rows)
headers
for row in rows:
        print(row)
f.close()
