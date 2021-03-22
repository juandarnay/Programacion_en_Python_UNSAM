# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
# hipoteca.py

print("Ejercicio 1.7: La hipoteca de David")

# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

# El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))

print("Ejercicio 1.8: Adelantos")

# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

# Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

# Cuando lo corras, este nuevo programa debería dar un pago total de 929965.62 en 342 meses.

# Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable mes y que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. Una posiblidad es inicializar mes en 0 y otra es inicializarla en 1. En el primer caso es problable que la variable salga del ciclo contando la cantidad de pagos que se hicieron, en el segundo, ¡es probable que salga contando la cantidad de pagos más uno!

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_con_adelanto = pago_mensual + 1000.00

while saldo > 0:
    if mes <= 12:
        saldo = saldo * (1+tasa/12) - pago_con_adelanto
        total_pagado = total_pagado + pago_con_adelanto
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1

print('Total pagado', round(total_pagado, 2), "en", mes - 1, "meses")

print("Ejercicio 1.9: Calculadora de adelantos")

# ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

# Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versatil. Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:

# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000

# Hacé que el programa tenga en cuenta estas variables para calcular el total a pagar apropiadamente.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
   
print('Total pagado', round(total_pagado, 2), "en", mes - 1, "meses")

# print("Ejercicio 1.10: Tablas")

# # Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. La salida debería verse aproximadamente así:

# # 1 2684.11 499399.22
# # 2 5368.22 498795.94
# # 3 8052.33 498190.15
# # 4 10736.44 497581.83
# # 5 13420.55 496970.98
# # ...
# # 308 874705.88 3478.83
# # 309 877389.99 809.21
# # 310 880074.1 -1871.53
# # Total pagado:  880074.1
# # Meses:  310

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes = 1
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000
# while saldo > 0:
#     if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
#         saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual + pago_extra
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
#     mes = mes + 1
#     print(mes, round(saldo, 1))

# print('Total pagado:', round(total_pagado, 1))
# print("Meses:", mes)

print("Ejercicio 1.11: Bonus")

# Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes  = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes = mes + 1
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin: 
        saldo = saldo * (1+tasa/12) - pago_extra - pago_mensual
        total_pagado = total_pagado + pago_extra + pago_mensual
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual 
        total_pagado = total_pagado + pago_mensual
    if saldo >= 0:
            print(mes, total_pagado, saldo)
    else: pass

print('Total pagado:',  total_pagado)
print('Meses', mes -1)