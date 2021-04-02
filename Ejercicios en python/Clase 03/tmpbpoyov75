import csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas) # yo aca no tuve que usar split , y en puse next(filas), no next(f)
        encabezados
        costo_total = 0.0
        for n_fila, fila in enumerate(filas, start= 1):
            #  record = {} esto no hace falta
            try:
                record = dict(zip(encabezados, fila)) # esto lo puse arriba del try (igual no se si cambia)
                ncajones = int(record['cajones'])
                precio = float(record['precio']) # aca va solo 'precio', si te quedo con /n es porque lo estabas leyendo mal arriba me parece
                costo_total += ncajones * precio
                # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return "El costo total es: $",costo_total