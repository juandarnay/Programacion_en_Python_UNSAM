'''
Ejercicio 2.5: Transformar un script en una función

Transformá el programa costo_camion.py (que
escribiste en el Ejercicio 2.2 de la sección
anterior) en una función
costo_camion(nombre_archivo). Esta función
recibe un nombre de archivo como entrada, lee
la información sobre los cajones que cargó el
camión y devuelve el costo de la carga de
frutas como una variable de punto flotante.
'''

def costo_camion(nombre_archivo):
    total_cajones = 0
    costo_frutas = 0
    costo_total = 0

with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        encabezados
        for linea in filas:
            fruta = filas[0]
            print(filas)
            cajones = int(filas[1])
            costo_unitario_frutas = float(filas[2])
            total_cajones += cajones
            costo_frutas += costo_unitario_frutas
            costo_total += (cajones * costo_unitario_frutas)
return costo_total
'''
Codigo anterior innecesario
    print("el total de cajones es:", total_cajones)
    print("el costo unitario de las frutas es:", round(costo_frutas, 2))
    print("Costo total:", round(costo_total, 2))
    f.close()
'''
