# Nombre del programa: Diccionarios - Corredor formula 1. <<algortimos>> (Reto 4)
# Programador: Juan Esteban Alarcón Miranda.
# Fecha: 01/07/2021
# Versión: 1
# Condiciones: día 1: valor; nDía: (valor*2)+10; día valor%3=0: valor/2
import os
os.system("cls")
print("Reto 4 - Formula 1.\n")
try:
    num_kilometrosDiaUno = int(input("¿Cuántos kilómetros recorrió el día 1?: \n"))
except ValueError:
    print("Dato erróneo, intente de nuevo.\n")
    num_kilometrosDiaUno = int(input("¿Cuántos kilómetros recorrió el día 1?: "))
while num_kilometrosDiaUno < 0:
    try:
      num_kilometrosDiaUno = int(input("¿Cuántos kilómetros recorrió el día 1?: \n"))
    except ValueError:
     print("Dato erróneo, intente de nuevo.\n")
     num_kilometrosDiaUno = int(input("¿Cuántos kilómetros recorrió el día 1?: "))
try:
    num_dias = int(input("¿Cuántos días duró el entrenamiento?: \n"))
except ValueError:
    print("Dato erróneo, intente de nuevo.\n")
    num_dias = int(input("¿Cuántos días duró el entrenamiento?: "))
while num_dias <= 0:
    try:
     num_dias = int(input("¿Cuántos días duró el entrenamiento?: \n"))
    except ValueError:
     print("Dato erróneo, intente de nuevo.\n")
     num_dias = int(input("¿Cuántos días duró el entrenamiento?: "))

def recorrido_formulaUno(num_kilometrosDiaUno,num_dias):
    recorridoFormulaUno = {}
    acumulado = num_kilometrosDiaUno
    recorridoFormulaUno[1] = [num_kilometrosDiaUno,num_kilometrosDiaUno] 
    kms_ = num_kilometrosDiaUno
    for _ in range(2,num_dias+1,1):
       dia = _
       if dia % 3 == 0:
           kmsRecorridos = (kms_ //2)
       else:
            kmsRecorridos = (kms_*2)+10
       kms_ = kmsRecorridos
       acumulado += kms_
       recorridoFormulaUno[_] = [kms_,acumulado]
    return recorridoFormulaUno

print("Impresión del diccionario <<recorridoFormulaUno>>.\n")
print("Día              kms Recorridos          Acumulado  ")
diccionario_recorridoFormulaUno = recorrido_formulaUno(num_kilometrosDiaUno,num_dias)
for clave,valor in diccionario_recorridoFormulaUno.items():
    print(clave,"                     ",valor[0],"                  ",valor[1],end="\t\n")
       