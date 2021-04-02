# import csv

# f = open(r'D:\Dropbox\Ciencia de datos\Programacion en Python UNSAM\Notas\01_ejercicios_python\Data\camion.csv')
# filas = csv.reader(f)
# encabezados = next(filas)
# encabezados
# fila = next(filas)
# fila
# list(zip(encabezados, fila))
# record = dict(zip(encabezados, fila))
# record

import csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        encabezados
        costo_total = 0.0
        for n_fila, fila in enumerate(filas, start= 1):
            try:
                record = dict(zip(encabezados, fila))
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
                # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return "El costo total es: $",costo_total