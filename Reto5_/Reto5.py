# Nombre del programa: Huevos (Reto 5)
# Programador: Juan Esteban Alarcón Miranda
# Fecha: 23/07/2021
# Versión: 1
import sys
import os
from tabulate import tabulate
import math 
import random
import time
os.system("cls")
#Funciones
def registroAutomatico(cantHuevos):
    huevos_auto={}
    error_datoPeso ="|---------------------------------------------------------|\n"+"|------------------------ ¡Error! ------------------------|\n"+"|¡Valor no válido! Ingrese únicamente dato numérico       |\n"+"|---------------------------------------------------------|\n"
    for _ in range(cantHuevos):
        while True:
         try:
          weight = random.uniform(10,100)
          huevos_auto[_]= weight
         except ValueError:
            print(error_datoPeso)
            huevos_auto[_]= random.uniform(10,100)
    Ordhuevos_auto=bubbleSort(huevos_auto)
    return Ordhuevos_auto
def registrar_huevos(cantidad_huevos):
    huevos_ = {}
    error_datoPeso ="|---------------------------------------------------------|\n"+"|------------------------ ¡Error! ------------------------|\n"+"|¡Valor no válido! Ingrese únicamente dato numérico|\n"+"|---------------------------------------------------------|\n"
    for _ in range(cantidad_huevos,1):
        try: 
          huevos_[_] = float(input(f"Digite el peso del huevo N°{_+1}: "))
        except ValueError:
             print(error_datoPeso) 
             huevos_[_] = float(input(f"Digite el peso del huevo N°{_+1}: "))
        while huevos_[_] <= 0 or  huevos_[_] > 200:
            try:
             huevos_[_] = float(input(f"Digite el peso del huevo N°{_+1}: "))
            except ValueError:
             print(error_datoPeso) 
             huevos_[_] = float(input(f"Digite el peso del huevo N°{_+1}: "))    
    return huevos_    
def clasificar_huevos(dict_huevos):
    huevos_clasificados = {}
    contA=0
    contAA=0
    contAAA=0
    contBC=0
    for _ in range(len(dict_huevos)):
        if dict_huevos[_] >= 53 and dict_huevos[_] <60:
            contA+=1
        elif dict_huevos[_] >=60 and dict_huevos[_] < 67:
            contAA += 1
        elif dict_huevos[_] >=67:
            contAAA+=1
        elif (dict_huevos[_] >=46 and dict_huevos[_] <= 53) or dict_huevos[_] < 46:
            contBC +=1
    huevos_clasificados={'A':contA,'AA':contAA,'AAA':contAAA,'BC':contBC}
    return huevos_clasificados
def clasificar_bandejas(dictHuevos):
    bandejas={}
    #Valores inciales, cantidad de huevos según categoría.
    eggA=clasificar_huevos(dictHuevos).get('A')
    eggAA=clasificar_huevos(dictHuevos).get('AA')
    eggAAA=clasificar_huevos(dictHuevos).get('AAA')
    eggBC=clasificar_huevos(dictHuevos).get('BC')
    total = eggA+eggAA+eggAAA+eggBC
    #Para tener en cuenta cantidad de huevos según tipo.
    huA=clasificar_huevos(dictHuevos).get('A')
    huAA=clasificar_huevos(dictHuevos).get('AA')
    huAAA=clasificar_huevos(dictHuevos).get('AAA')
    huBC=clasificar_huevos(dictHuevos).get('BC')
    huevoA=0
    huevoAA=0
    huevoAAA=0
    huevoBC=0
    if eggA//30 >=1:
        eggA=eggA//30
        huevoA=math.floor(eggA)
        a=str(huevoA)+"(x24 UND)"
    else:
        huevoA=0
        a=str(huevoA)+"(x24 UND)"
    if eggAA//24 >=1:
        eggAA=eggAA//24
        huevoAA=math.floor(eggAA)
        aa = str(huevoAA)+" (x30 UND)"
    else:
        huevoAA=0
        aa = str(huevoAA)+" (x30 UND)"
    if eggAAA//12 >=1:
        eggAAA=eggAAA//12
        huevoAAA=math.floor(eggAAA)
        aaa=str(huevoAAA)+" (x12 UND)"
    else:
        huevoAAA=0
        aaa=str(huevoAAA)+" (x12 UND)"
    if eggBC // 30 >=1:
        eggBC=eggBC//30
        huevoBC=math.floor(eggBC)
        bc=str(huevoBC)+" (x30 UND)"
    else:
        eggBC=0
        bc=str(huevoBC)+" (x30 UND)"
    bandejas={'hA':a,'hAA':aa,'hAAA':aaa,'hBC':bc,'Total':total}
    return bandejas
def process_data(file_):
    data=[]
    for __ in file_:
        data.append(float(__.replace("\n","")))
    clasificar_huevos(data)
def readFile():
    while True:
        try:
         pathFile = input("Ingrese ruta completa del archivo: ")
         file_=open(pathFile,'r',encoding="utf-8")
         process_data(file_)
         break
        except FileNotFoundError:
            print("Filename does not exists.")
def bubbleSort(huevos_):
    for x in range(0,len(huevos_)-1,1):
        for k in range(x+1,len(huevos_),1):
            if huevos_[x] > huevos_[k]:
                aux=huevos_[x]
                huevos_[x]=huevos_[k]
                huevos_[k]=aux
    return huevos_ 

def clearScreen():
    if os.name=="nt" or os.name=="ce" or os.name=="dos":
        os.system("cls")
    elif os.name=="posix":
        os.system("clear") 
def main():
    menu = "|---------------------------------------------------------|\n"+"|            MODO DE EJECICIÓN DEL PROGRAMA               |\n"+"|---------------------------------------------------------|\n"+"| Opción 0 |: SALIR                                       |\n"+"| Opción 1 |: MODO DEMOSTRACIÓN (Información Aleatoria)   |\n"+"| Opción 2 |: REGISTRO MANUAL (Ingresar Información)      |\n"+"| Opción 3 |: REGISTRO A TRAVÉS DE ARCHIVO.(Carga Archivo)|\n"+"|---------------------------------------------------------|\n"+"Digite la opción :| "
    error_dato ="|---------------------------------------------------------|\n"+"|------------------------ ¡Error! ------------------------|\n"+"|¡Valor no válido! Ingrese únicamente dato numérico|\n"+"|---------------------------------------------------------|\n"
    errorVacio ="|---------------------------------------------------------|\n"+"|------------------------ ¡Error! ------------------------|\n"+"|¡Diccionario vacío! Debe registrar datos primero antes de usar ésta función.  |\n"+"|---------------------------------------------------------|\n"
    try:
     op=int(input(menu))
    except ValueError:
        print(error_dato)
        op=int(input(menu))
    while op < 0 or op=="":
        try:
         op=int(input(menu))
        except ValueError:
         print(error_dato)
         op=int(input(menu))
    while op >=0 and op <= 3:
        if op == 0:
            try:
             decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
            except ValueError:
             print("Dato erróneo, intente nuevamente.\n")
             decision = input("¿Está seguro que desea finalizar el programa?. S/N.\n").upper()
            while decision != "S" and decision != "N":
             try:
                decision = input("| ¿Está seguro que desea finalizar el programa?. S/N |:\n").upper()
             except ValueError:
                print(error_dato)
                decision = input("| ¿Está seguro que desea finalizar el programa?. S/N |:\n").upper()
            if decision == "S":
             print("*********************************Finalizando...*********************************\n")
             time.sleep(2)
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
        elif op == 1:
            demo="|---------------------------------------------------------|\n"+"|                     MODO DEMOSTRACIÓN                   |\n"+"|---------------------------------------------------------|\n"
            print(demo)
            try:
                cantHuevos__=int(input("| Digite cantidad de huevos a clasificar  :| "))
            except ValueError:
                print(error_dato)
                cantHuevos__=int(input("| Digite cantidad de huevos a clasificar  :|  "))
            while cantHuevos__<=0:
                try:
                 cantHuevos__=int(input("| Digite cantidad de huevos a clasificar  :| "))
                except ValueError:
                 print(error_dato)
                 cantHuevos__=int(input("| Digite cantidad de huevos a clasificar  :|  "))
            automatico = registroAutomatico(cantHuevos__)
            print("| ¿Desea imprimir lista huevos y pesos?")
            try:
             decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0    :| "))
            except ValueError:
                print(error_dato)
                decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            while decision_print != 1 and decision_print != 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            if decision_print == 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                while decision_print != 1 and decision_print != 0:
                 try:
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                 except ValueError:
                  print(error_dato)
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            else:
                huevosClasificados__=clasificar_huevos(automatico)
                huevosA=huevosClasificados__.get("A")
                huevosAA=huevosClasificados__.get("AA")
                huevosAAA=huevosClasificados__.get("AAA")
                huevosBC=huevosClasificados__.get("BC")
                #Bandejas.
                bandClasificada=clasificar_bandejas(huevosClasificados__)
                bandejasA=bandClasificada.get("hA")
                bandejasAA=bandClasificada.get("hAA")
                bandejasAAA=bandClasificada.get("hAAA")
                bandejasBC=bandClasificada.get("hBC")
                total__=bandClasificada.get("Total")
                automatic_eggs = {"TIPO_HUEVO":["A","AA","AAA","BC"],"CANTIDAD":[huevosA,huevosAA,huevosAAA,huevosBC],"NUMERO_BANDEJAS":[bandejasA,bandejasAA,bandejasAAA,bandejasBC]}
                print(tabulate(automatic_eggs,headers=["TIPO HUEVO","CANTIDAD","NÚMERO BANDEJAS"],tablefmt="grid",numalign="center",stralign="center"))
                imp_total = "-------------------------------------------------------\n"+f"             TOTAL: {str(total__)} \n"+"-------------------------------------------------------\n"
                print(imp_total)
                time.sleep(2)
                try:
                 op=int(input(menu))
                except ValueError:
                 print(error_dato)
                 op=int(input(menu))
                while op < 0 or op=="":
                 try:
                  op=int(input(menu))
                 except ValueError:
                  print(error_dato)
                  op=int(input(menu))
        elif op == 2:
            print("|---------------------------------------------------------|\n"+"|               INGRESO MANUAL DE LOTE DE HUEVOS          |\n"+"|-------------------------------------------------------|\n")
            try:
             cantHuevos_=int(input("| Digite cantidad de huevos a clasificar  :| "))
            except ValueError:
             print(error_dato)
             cantHuevos_=int(input("| Digite cantidad de huevos a clasificar  :| "))
            while cantHuevos_<=0 or cantHuevos_ == 1:
                try:
                 cantHuevos_=int(input("| Digite cantidad de huevos a clasificar  :| "))
                except ValueError:
                 print(error_dato)
                 cantHuevos_=int(input("| Digite cantidad de huevos a clasificar  :| "))
            huevosRegistrados=registrar_huevos(cantHuevos_)
            time.sleep(2)
            print("| ¿Desea imprimir lista huevos y pesos?")
            try:
             decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0    :| "))
            except ValueError:
                print(error_dato)
                decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            while decision_print != 1 and decision_print != 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            if decision_print == 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                while decision_print != 1 and decision_print != 0:
                 try:
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                 except ValueError:
                  print(error_dato)
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            else:
                try:
                 huevosClasificados = clasificar_huevos(huevosRegistrados)
                 huevos_A= huevosClasificados.get("A")
                 huevos_AA=huevosClasificados.get("AA")
                 huevos_AAA=huevosClasificados.get("AAA")
                 huevos_BC=huevosClasificados.get("BC")
                 bandejas=clasificar_bandejas(huevosClasificados)
                 bandejaA =bandejas.get("hA")
                 bandejaAA=bandejas.get("hAA")
                 bandejaAAA=bandejas.get("hAAA")
                 bandejaBC=bandejas.get("hBC")
                 total=bandejas.get("Total")
                except KeyError:
                    print(errorVacio)
                    time.sleep(2)
                    try:
                     op=int(input(menu))
                    except ValueError:
                     print(error_dato)
                     op=int(input(menu))
                    while op < 0 or op=="":
                     try:
                      op=int(input(menu))
                     except ValueError:
                      print(error_dato)
                      op=int(input(menu))
                impresion_huevos = {"TIPO_HUEVO":["A","AA","AAA","BC"],"CANTIDAD":[huevos_A,huevos_AA,huevos_AAA,huevos_BC],"NUMERO_BANDEJAS":[bandejaA,bandejaAA,bandejaAAA,bandejaBC]}
                #Impresión tabla huevos.
                print(tabulate(impresion_huevos,headers=["TIPO HUEVO","CANTIDAD","NÚMERO BANDEJAS"],tablefmt="fancy_grid",numalign="center",stralign="center"))
                imp_total = "-------------------------------------------------------\n"+f"             TOTAL: {str(total)} \n"+"-------------------------------------------------------\n"
                print(imp_total)
                try:
                 op=int(input(menu))
                except ValueError:
                 print(error_dato)
                 op=int(input(menu))
                while op < 0 or op=="":
                 try:
                  op=int(input(menu))
                 except ValueError:
                  print(error_dato)
                  op=int(input(menu))
        elif op==3:
            print("Por favor espere....\n")
            time.sleep(2)
            file__ = readFile()
            eggs_file = {}
            count=0
            for ___ in file__:
                eggs_file[count]=___
                count+=1
            huevos_clasificados_archivo=clasificar_huevos(eggs_file)
            bandejas_clasificadas=clasificar_bandejas(huevos_clasificados_archivo)
            try:
            #Cantidad huevos según tipo.
             huevitosA=huevos_clasificados_archivo.get("A")
             huevitosAA=huevos_clasificados_archivo.get("AA")
             huevitosAAA=huevos_clasificados_archivo.get("AAA")
             huevitosBC=huevos_clasificados_archivo.get("BC")
            #Cantidad huevos según tipo.
             bandejitasA=bandejas_clasificadas.get("hA")
             bandejitasAA=bandejas_clasificadas.get("hAA")
             bandejitasAAA=bandejas_clasificadas.get("hAAA")
             bandejitasBC=bandejas_clasificadas.get("hBC")
             total_huevitos=bandejas_clasificadas.get("Total")
            except KeyError:
                print(errorVacio)
                time.sleep(2)
                try:
                    op=int(input(menu))
                except ValueError:
                    print(error_dato)
                    op=int(input(menu))
                    while op < 0 or op=="":
                     try:
                      op=int(input(menu))
                     except ValueError:
                      print(error_dato)
                      op=int(input(menu))
            time.sleep(2)
            print("| ¿Desea imprimir lista huevos y pesos?")
            try:
             decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0    :| "))
            except ValueError:
                print(error_dato)
                decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            while decision_print != 1 and decision_print != 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            if decision_print == 0:
                try:
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                except ValueError:
                 print(error_dato)
                 decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                while decision_print != 1 and decision_print != 0:
                 try:
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
                 except ValueError:
                  print(error_dato)
                  decision_print=int(input("| Imprimir digite 1, de lo contrario digite 0 :| "))
            else:
                huevitos_archivo={"TIPO_HUEVO":["A","AA","AAA","BC"],"CANTIDAD":[huevitosA,huevitosAA,huevitosAAA,huevitosBC],"BANDEJAS":[bandejitasA,bandejitasAA,bandejitasAAA,bandejitasBC]}
                print(tabulate(huevitos_archivo,headers=["TIPO HUEVO","CANTIDAD","NÚMERO BANDEJAS"],tablefmt="fancy_grid",numalign="center",stralign="center"))
                imp_total = "-------------------------------------------------------\n"+f"             TOTAL: {str(total)} \n"+"-------------------------------------------------------\n"
                print(imp_total)
            time.sleep(2)
            try:
                op=int(input(menu))
            except ValueError:
             print(error_dato)
             op=int(input(menu))
            while op < 0 or op=="":
             try:
                op=int(input(menu))
             except ValueError:
                print(error_dato)
                op=int(input(menu))              
os.system("cls")        
main()