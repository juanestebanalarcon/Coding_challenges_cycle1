# Nombre del programa: Calculo de nota asignatura <<algortimos>> (Reto 1)
# Programador: Juan Esteban Alarcón Miranda
# Fecha: 10/06/2021
# Versión: 1
print("A continuación ingrese los datos solicitados para calcular la calificación para la asignatura <<Algoritmos>>")
print()
print("Digite a continuación la nota obtenida en cada una de los tres parciales: ")
print()
TareaUno = float(input("Ingrese nota para la calificación parcial 1: (0.0 a 5.0) "))
while TareaUno <= 0.0 or TareaUno > 5.0:
    TareaUno = float(input("Ingrese nota para la calificación parcial 1: (0.0 a 5.0) "))
TareaDos = float(input("Ingrese nota para la calificación parcial 2: (0.0 a 5.0)"))
while TareaDos <= 0.0 or TareaDos > 5.0:
    TareaDos = float(input("Ingrese nota para la calificación parcial 2: (0.0 a 5.0) "))
TareaTres = float(input("Ingrese nota para la calificación parcial 3: (0.0 a 5.0) "))
while TareaTres <= 0.0 or TareaTres > 5.0:
    TareaTres = float(input("Ingrese nota para la calificación parcial 3: (0.0 a 5.0) "))
promedioCalificacionesParciales = (TareaUno + TareaDos + TareaTres)/3
examenFinal = float(input("Ingrese calificación del examen final: "))
while examenFinal <= 0.0 or examenFinal > 5.0:
    examenFinal = float(input("Ingrese calificación del examen final: "))

trabajoFinal = float(input("Ingrese calificación del trabajo final: "))
while trabajoFinal <= 0.0 or trabajoFinal > 5.0:
    trabajoFinal = float(input("Ingrese calificación del trabajo final: "))

nota = (promedioCalificacionesParciales * 0.55) + (examenFinal * 0.3) + (trabajoFinal * 0.15)
print(f"{nota}")