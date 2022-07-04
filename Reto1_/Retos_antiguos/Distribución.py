# Datos de validación
# Entrada 100000
# Salida 20000.0 15000.0 10000.0 15000.0 50000.0
# Entrada 500000
# Salida 100000.0 75000.0 50000.0 75000.0 250000.0
# Entrada 2550000
# Salida 510000.0 382500.0 255000.0 382500.0 1275000.0
salario = float(input("Digite salario recibido: "))
while salario <= 0:
    salario = float(input("Digite salario recibido: "))

compraAlimentos = salario * 0.2 
compraPasajes = salario * 0.15 
compra_Boletos_cine = salario * 0.1
compraLibros = salario * 0.15
pagoAlquiler = salario * 0.4
print(str(compraAlimentos) + " "+ str(compraPasajes) + " "+ str(compra_Boletos_cine) + " "+ str(compraLibros) + " "+ str(pagoAlquiler))