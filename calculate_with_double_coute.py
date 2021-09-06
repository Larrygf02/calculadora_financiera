import math
from datetime import datetime, timedelta
print("SIMULADOR DE PRESTAMO - CUOTA DOBLE")
print("===================================")

monto = float(input("Ingrese la cantidad a solicitar: "))
numero_cuotas = int(input("Ingrese la cantidad de cuotas: "))
tasa = float(input("Ingrese la tasa en (%): "))
tasa = tasa / 100
cuotas_pagadas = 0
saldo_capital = monto
tasa_diaria = (math.pow((1+tasa), (1/360)) - 1)
print(tasa_diaria)
fecha_1 = '2015-06-11'
fecha_2 = '2015-07-11'
days = [i*30 for i in range(1,numero_cuotas)]
fecha_desembolso = "2015-06-11"
days_pago = []
day_pago = datetime.strptime(fecha_desembolso, "%Y-%m-%d")
fsas = []
days_acumulados = 0
for i in range(1, numero_cuotas+1):
    days_acumulados += 30
    day_pago = day_pago + timedelta(days=30)
    days_pago.append(day_pago)
    if day_pago.month == 6 or day_pago.month == 12:
        fsa = math.pow((1+tasa_diaria), -days_acumulados) * 2
    else:
        fsa = math.pow((1+tasa_diaria), -days_acumulados)
    fsas.append(fsa)

print(fsas)
cuota = monto / sum(fsas)
cuota = round(cuota, 2)
saldo_deudor = monto
for i in range(1, numero_cuotas+1):
    interes = saldo_deudor * (math.pow((1+tasa_diaria), 30) - 1)
    if days_pago[i-1].month == 6 or days_pago[i-1].month == 12:
        cuota_mes = cuota * 2
    else:
        cuota_mes = cuota
    amortizacion = cuota_mes - interes
    saldo_deudor -= amortizacion
    print("MES ", i, days_pago[i-1].strftime("%Y-%m-%d"))
    print("======================")
    print("Amortizacion", round(amortizacion,2))
    print("Interes", round(interes,2))
    print("Cuota", round(cuota_mes,2))
    print("Saldo deudor", round(saldo_deudor,2))
