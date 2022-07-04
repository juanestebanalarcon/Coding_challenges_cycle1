# Nombre del programa: Calculo de nota asignatura <<algortimos>> (Reto 1)
# Programador: Juan Esteban Alarcón Miranda
# Fecha: 10/06/2021
# Versión: 1
notaUno = float(input())
notaDos = float(input())
notaTres = float(input())
promNotaParciales = ((notaUno + notaDos + notaTres ) / 3)
examenFinal = float(input())
trabajoFinal = float(input())
notaFinal = ((promNotaParciales * 0.55) + (examenFinal * 0.3) + (trabajoFinal * 0.15))
print(f"{notaFinal}")