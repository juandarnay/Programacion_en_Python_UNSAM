# Ejercicio 3.3: Un ejemplo práctico de enumerate()

# Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. Usando enumerate(), modificá tu programa costo_camion.py de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta.

def costo_camion(nombre_archivo):
    total_cajones = 0
    costo_frutas = 0
    costo_total = 0

    filas = open (nombre_archivo, "rt")
    encabezados = next(filas).split(",")
    for n_fila, fila in enumerate(filas, start = 1):
        try:
            fila = fila.split(",")
            fruta = fila[0]
            cajones = int(fila[1])
            costo_unitario_frutas = float(fila[2])
            total_cajones += cajones
            costo_frutas += costo_unitario_frutas
            costo_total += (cajones * costo_unitario_frutas)
        except ValueError:
            print(f'Fila {n_fila}: no pude interpretar: {fila}')
    return costo_total
    f.close()
'''
Codigo anterior innecesario
    print("el total de cajones es:", total_cajones)
    print("el costo unitario de las frutas es:", round(costo_frutas, 2))
    print("Costo total:", round(costo_total, 2))
    f.close()
'''