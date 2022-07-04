# Nombre del programa: Menú operaciones - agencia de viajes. <<algortimos>> (Reto 3)
# Programador: Juan Esteban Alarcón Miranda.
# Fecha: 24/06/2021
# Versión: 1
import os   
import sys 
os.system("cls")
print(" Programa - Agencia de viajes. \n")
#Declaración de las listas.
pasajeros = []
ciudades = []
#Declaración de la variable que contendrá el menú de opciones.
menu = "1. Agregar pasajero. \n" + "2. Agregar ciudad. \n" + "3. Consultar ciudades a las que viaja un pasajero. \n"+"4. Consultar cantidad de pasajeros que viajaron a una determinada Ciudad. \n"+"5. Consultar valor recaudado por los viajes realizados. \n"+"6. Consultar valor recaudado por cada Ciudad.\n"+"7. Salir. \n"
try:
    opcion = int(input("Digite una opción: \n \n" + menu))
except ValueError:
    print("Dato erróneo, intente nuevamente: \n")
    opcion = int(input("Digite una opción: \n \n" + menu))
while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
#Estructura switch simulada en Python.
while opcion <= 7:
    #Agregar pasajero
    if opcion == 1:
        try:
            cant_pasajeros = int(input("¿Cuántos pasajeros desea agregar?: "))
        except ValueError:
            print("Dato erróneo, intente nuevamente.")
            cant_pasajeros = int(input("¿Cuántos pasajeros desea agregar?: "))
        while cant_pasajeros <= 0:
            try:
                cant_pasajeros = int(input("¿Cuántos pasajeros desea agregar?: "))
            except ValueError:
                print("Dato erróneo, intente nuevamente.")
                cant_pasajeros = int(input("¿Cuántos pasajeros desea agregar?: "))
        if cant_pasajeros == 1:
            nombre = input("Ingrese nombre y apellido del pasajero: ")
            try:
             documento_ = int(input("Ingrese número de documento: "))
            except ValueError:
                print("Dato erróneo, intente nuevamente.")
                documento_ = int(input("Ingrese número de documento: "))
            while documento_ <= 0:
                try:
                   documento_ = int(input("Ingrese número de documento: "))
                except ValueError:
                   print("Dato erróneo, intente nuevamente.")
                   documento_ = int(input("Ingrese número de documento: "))
            ciudadDestino = input("Ingrese destino: ")
            pasajeros.append([nombre,documento_,ciudadDestino])
        else:
         for _ in range(cant_pasajeros):
            pasajeros.append([])
         for __ in range(cant_pasajeros):
            print(f"Ingrese información del pasajero {__+1} \n")
            try:
                pasajeros[__].append(input("Ingrese nombre y apellido del pasajero: "))
            except ValueError:
                print("Dato erróneo, intente nuevamente. \n")
                pasajeros[__].append(input("Ingrese nombre y apellido del pasajero: "))
            try:
                pasajeros[__].append(int(input(f"Ingrese número de documento del pasajero: ")))
            except ValueError:
                print("Dato erróneo, intente nuevamente. \n")
                pasajeros[__].append(int(input(f"Ingrese número de documento del pasajero: ")))
            try:
                pasajeros[__].append(input("Ingrese destino: ").upper())
            except ValueError:
                print("Dato erróneo, intente nuevamente. \n")
                pasajeros[__].append(input("Ingrese destino: ").upper())
        try:
            opcion = int(input("Digite una opción: \n \n" + menu))
        except ValueError:
            print("Dato erróneo, intente nuevamente: \n")
            opcion = int(input("Digite una opción: \n \n" + menu))
        while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Agregar ciudad
    elif opcion == 2:
            try:
                cant_ciudades = int(input("¿Cuántas ciudades desea agregar?: "))
            except ValueError:
                print("Dato erróneo, intente nuevamente.")
                cant_ciudades = int(input("¿Cuántas ciudades desea agregar?: "))
            while cant_ciudades <=0:
                try:
                    cant_ciudades = int(input("¿Cuántas ciudades desea agregar?: "))
                except ValueError:
                    print("Dato erróneo, intente nuevamente.")
                    cant_ciudades = int(input("¿Cuántas ciudades desea agregar?: "))
            if cant_ciudades == 1:
                nombre_ciudad = input("Digite nombre de la ciudad: ").upper()
                pais_origen = input("Digite país de origen: ").upper()
                try:
                    tiqueteCosto = int(input("Digite precio del tiquete: $"))
                except ValueError:
                    print("Dato erróneo, intente nuevamente.\n")
                    tiqueteCosto = int(input("Digite precio del tiquete: $"))
                ciudades.append([nombre_ciudad,pais_origen,tiqueteCosto])
            else:
             for m in range(cant_ciudades):
                ciudades.append([])
             for k in range(cant_ciudades):
                print(f"Ingrese información de la ciudad {k+1} \n")
                try:
                  ciudades[k].append(input("Digite nombre de la ciudad: ").upper())
                except ValueError:
                  print("Dato erróneo, intente nuevamente.\n")
                  ciudades[k].append(input("Digite nombre de la ciudad: ").upper())
                try:
                  ciudades[k].append(input("Digite país de origen: ").upper())
                except ValueError:
                  print("Dato erróneo, intente nuevamente.\n")
                  ciudades[k].append(input("Digite país de origen: ").upper())
                try:
                  ciudades[k].append(int(input("Digite precio del tiquete: $")))
                except ValueError:
                  print("Dato erróneo, intente nuevamente.\n")
                  ciudades[k].append(int(input("Digite precio del tiquete: $"))) 
            try:
              opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
              print("Dato erróneo, intente nuevamente: \n")
              opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Consultar ciudades a las que viaja un pasajero.
    elif opcion == 3:
        if not pasajeros:
            print("La lista está vacía, debe agregar datos primero para poder usar esta función.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
        else:
            try:
                documento = int(input("Digite documento a consultar: \n"))
            except ValueError:
                print("Dato erróneo, intente nuevamente. \n")
                documento = int(input("Digite documento a consultar: \n"))
            while documento <= 0:
                try:
                    documento = int(input("Digite documento a consultar: \n"))
                except ValueError:
                    print("Dato erróneo, intente nuevamente. \n")
                    documento = int(input("Digite documento a consultar: \n"))   
            for pas in pasajeros:
                if pas[1] == documento:
                    print(f"El pasajero con número de documento {documento} tiene como destino {pas[2]}")
                else:
                    print(f"El documento {documento} no existe.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Consultar cantidad de pasajeros que viajaron a una determinada ciudad.
    elif opcion == 4:
        counter_ciudad = 0
        if not pasajeros:
            print("La lista está vacía, debe agregar datos primero para poder usar esta función.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
        else:
            try:
                ciudad = input("Digite ciudad a consultar: \n").upper()
            except ValueError:
                print("Dato erróneo, intente nuevamente.\n")
                ciudad = input("Digite ciudad a consultar: \n").upper()
            for pasa in pasajeros:
                if pasa[2] == ciudad:
                    counter_ciudad += 1
            print(f"La cantidad de pasajeros que han viajado a {ciudad} es: {counter_ciudad} \n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Consultar valor recaudado por los viajes realizados.
    elif opcion == 5:
        recaudo = 0
        destino_ = " "
        if (not ciudades) or (not pasajeros):
            print("Una de las listas está vacía, debe agregar datos primero para usar esta función.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
        else:
            for pasaj in pasajeros:
                destino_ = pasaj[2]
                for ciud in ciudades:
                    ciudad_ = ciud[0]
                    if ciudad_ == destino_:
                        recaudo += ciud[2]
            print(f"El valor recaudado de los viajes realizados fue: ${recaudo}.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Consultar valor recaudado por cada Ciudad.
    elif opcion == 6:
        if (not ciudades) or (not pasajeros):
            print("Una de las listas está vacía, debe agregar datos primero para usar esta función.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
        else:
            recaudo_ = 0
            destino = " "
            precio_ = 0
            for _ in ciudades:
                destino = _[0]
                precio_ = _[2]
                for __ in pasajeros:
                    if destino == __[2]:
                        recaudo_ += precio_
                print(f"La ciudad {_[0]} ha recaudado ${recaudo_}.\n")
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
    #Salir
    elif opcion == 7:
        try:
            decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
        except ValueError:
            print("Dato erróneo, intente nuevamente.\n")
            decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
        while decision != "S" and decision != "N":
            try:
                decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
            except ValueError:
                print("Dato erróneo, intente nuevamente.\n")
                decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
        if decision == "S":
            print("Finalizando...\n")
            sys.exit()
        else:    
            try:
                opcion = int(input("Digite una opción: \n \n" + menu))
            except ValueError:
                print("Dato erróneo, intente nuevamente: \n")
                opcion = int(input("Digite una opción: \n \n" + menu))
            while opcion <= 0 or opcion == " ":
                try:
                    opcion = int(input("Digite una opción: \n \n" + menu))
                except ValueError:
                    print("Dato erróneo, intente nuevamente: \n")
                    opcion = int(input("Digite una opción: \n \n" + menu))
