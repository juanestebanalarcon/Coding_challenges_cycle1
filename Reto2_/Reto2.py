# Nombre del programa: Calculo de decisiones <<CEO empresa tecnológica (Reto 2)
# Programador: Juan Esteban Alarcón Miranda
# Fecha: 15/06/2021
# Versión: 1
mobiliario = 2000
equipo = 5000
prestamo = 0
deuda = 0
saldo_actual = 0
insumos = incentivos = 0
print("***Algoritmo empresa tecnológica***")
print()
saldo = int(input("Ingrese saldo: $"))
#Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que su nuevo saldo sea de $10000 dólares.
#Si su capital tiene actualmente un saldo positivo pedirá un préstamo bancario para tener un nuevo saldo de $20000 dólares
if saldo < 0:
    prestamo = 10000
    deuda = prestamo + (-saldo)
    saldo_actual = (prestamo - (mobiliario + equipo))
    insumos = saldo_actual /2
    incentivos = saldo_actual /2
    print(f"{insumos}")
    print(f"{incentivos}")
    print(f"{deuda}")
elif saldo > 0 and saldo < 20000:
    prestamo = 20000 
    deuda = prestamo - saldo
    saldo_actual = (prestamo - (mobiliario + equipo))
    insumos = saldo_actual/2
    incentivos = saldo_actual/2
    print(f"{insumos}")
    print(f"{incentivos}")
    print(f"{deuda}")
else:
    saldo_actual = (saldo - (mobiliario + equipo))
    insumos = saldo_actual/2
    incentivos = saldo_actual/2
    print(f"{insumos}")
    print(f"{incentivos}")