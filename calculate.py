print("SIMULADOR DE PRESTAMO")
print("=====================")
monto = float(input("Ingrese la cantidad a solicitar: "))
numero_cuotas = int(input("Ingrese la cantidad de cuotas: "))
tasa = float(input("Ingrese la tasa en (%): "))
tasa = tasa / 100
cuota = ((((1 + tasa)**numero_cuotas) * tasa) / (((1 + tasa)**numero_cuotas) -1)) * monto
cuotas_pagadas = 0
saldo_capital = monto
while cuotas_pagadas < numero_cuotas:
    cuotas_pagadas += 1
    print("Cuota", cuotas_pagadas)
    print("====================")
    print("Cuota: ", round(cuota,2))

    interes = tasa * saldo_capital
    print("Interes: ", round(interes,2))

    amortizacion = cuota - interes
    print("Amortizacion: ", round(amortizacion,2))

    saldo_capital = saldo_capital -amortizacion
    print("Saldo Capital:", round(saldo_capital,2))