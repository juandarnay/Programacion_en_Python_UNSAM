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
    if saldo < 0.00:
            saldo = 0.00
            total_pagado = total_pagado + 0.00
    if saldo >= 0:
            print(mes, total_pagado, saldo)
    else: pass

print('Total pagado:',  total_pagado)
print('Meses:', mes)
