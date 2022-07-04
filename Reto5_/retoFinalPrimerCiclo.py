'''
Fundamentos de Programación UNAB - MinTic
Reto No. 5 
Programa: A partir de un conjunto de datos relacionados con el peso de un conjunto de huevos, clasificar los huevos por 
tipo A, AA, AAA, y B y C y calcular cuántas bandejas de huevos se pueden obtener por cada una de las clasificaciones
Programado por:Luz Dary Ocampo Cano
Fecha:23 de julio de 2021
'''

import os
import math
from tabulate import tabulate
import random

huevos=[]
totalhuevos=0


#Función para limpiar pantalla

def limpiarPantalla():
    if os.name=="nt" or os.name=="ce" or os.name=="dos":
        os.system("cls")
    if os.name=="posix":
        os.system("clear")

#Menú Principal 

def menuPrincipal():
    print("---------------------------------------")
    print(" DISTRIBUIDORA DE HUEVOS LA GRANJA ")
    print("---------------------------------------")
    print("")
    print("1. Registrar peso de huevos manualmente")
    print("2. Registrar peso de huevos a través de un archivo")
    print("3. Simulación clasificación de huevos con cálculo aleatorio")
    print("4. Salir")
    print("")
    print("---------------------------------------")

#Función para Leer Archivo 

def leerArchivo():
       
    while True:
        try:        
            rutaArchivo= input('Digite el nombre del archivo (ruta completa))  : ')
            archivo=open(rutaArchivo,"r",encoding="utf-8")
            #archivo=open("/Users/000052649/Desktop/cantidadhuevos1.txt","r",encoding="utf-8")
            procesarInformación(archivo)
            break    
        except FileNotFoundError:
            print ("Error! El nombre del archivo no existe")

    leerArchivo()

#Función para procesar archivo de lectura               
    
def procesarInformación(archivo):                   
    datos=[]
    for i in archivo:
        datos.append(float(i.replace("\n","")))
    clasificacionHuevos(datos)


#Función para ordenar los pesos de menor a mayor 

def ordenamiento_burbuja(huevos):
    for i in range (0,len(huevos)-1,1):
        for j in range (i+1,len(huevos),1):
            if huevos[i]>huevos[j]:  
                t=huevos[i]
                huevos[i]=huevos[j]
                huevos[j]=t
    return huevos

#Función para clasificar los huevos 

def clasificacionHuevos(huevos):
    huevos_A=0
    huevos_AA=0
    huevos_AAA=0
    huevos_BC=0
        
    for i in range (len(huevos)):      
        if huevos[i] >= 53 and huevos[i] < 60:
            huevos_A += 1
            #print(f'A: {huevos_A}')
        elif huevos[i] >= 60 and huevos[i] < 67:
            huevos_AA += 1
            #print(f'AA: {huevos_AA}')
        elif huevos[i] >= 67:
            huevos_AAA += 1
            #print(f'AAA: {huevos_AAA}')
        elif huevos[i] < 53:
            huevos_BC += 1
            #print(f'BC: {huevos_BC}')
    
    clasificacionHuevos={'huevos_A':huevos_A,'huevos_AA':huevos_AA,'huevos_AAA':huevos_AAA,'huevos_BC':huevos_BC}         
    #print(clasificacionHuevos)
    
    huevos_A=clasificacionHuevos.get('huevos_A')
    huevos_AA=clasificacionHuevos.get('huevos_AA')
    huevos_AAA=clasificacionHuevos.get('huevos_AAA')
    huevos_BC=clasificacionHuevos.get('huevos_BC')
           
    calcularBandejas(huevos_A, huevos_AA, huevos_AAA, huevos_BC)
    
  
#Función para calcular bandejas

def calcularBandejas(huevos_A, huevos_AA, huevos_AAA, huevos_BC):
    
    if huevos_A / 30 >= 1:
        huevosA = huevos_A / 30
        A = math.floor(huevosA)
        #print(f'bandeja_A: {A}')
    else:
        A = 0
        #print(f'bandeja_A: {A}')

    if huevos_AA /24 >= 1:
        huevosAA = huevos_AA / 24
        AA = math.floor(huevosAA)
        #print(f'bandejas_AA: {AA}')
    else:
        AA = 0
        #print(f'bandejas_AA: {AA}')

    if huevos_AAA /12 >= 1:
        huevosAAA = huevos_AAA / 12
        AAA = math.floor(huevosAAA)
        #print(f'bandejas_AAA: {AAA}')
    else:
        AAA = 0
        #print(f'bandejas_AAA: {AAA}')

    if huevos_BC / 30 >= 1:
        huevosBC = huevos_BC / 30
        BC = math.floor(huevosBC)
        #print(f'bandejas_BC: {BC}')
    else:
        BC = 0
        #print(f'bandejas_BC: {BC}')

    calcularBandejas={'huevos_A':A,'huevos_AA':AA,'huevos_AAA':AAA,'huevos_BC':BC} 
    totalhuevos=huevos_A+huevos_AA+huevos_AAA+huevos_BC
  
#Impresión con Tabulate
    
    limpiarPantalla()
    
    misHuevos={"TIPO DE HUEVO": ["A", "AA", "AAA", "BC"], "CANTIDAD":[huevos_A,huevos_AA,huevos_AAA,huevos_BC], "NUMERO DE BANDEJAS":[A,AA,AAA,BC] }
     
    print(tabulate(misHuevos, headers=["TIPO DE HUEVO", "CANTIDAD", "NUMERO DE BANDEJAS"], tablefmt="fancy_grid", numalign="center",stralign="center"))
    print("-------------------------------------------------------")
    print("TOTAL DE HUEVOS: ", totalhuevos)
    print("-------------------------------------------------------")
    print()
    
#Impresión tradicional
'''
    limpiarPantalla()   
    print("--------------------------------------------------------------------------------------")
    print(                    "CLASIFICACIÓN DE HUEVOS -- DISTRIBUIDORA DE HUEVOS LA GRANJA"                )
    print("--------------------------------------------------------------------------------------")
    print()
    print("\n",
          "Huevos Tipo: A ",    "|" ," cantidad: ", huevos_A," huevos" ,    "|","Número de badejas: ",A, "(x30 UND)","\n", 
          "Huevos Tipo: AA ",   "|" ," cantidad: ", huevos_AA," huevos" ,   "|","Número de badejas: ",AA ,"(x24 UND)","\n", 
          "Huevos Tipo: AAA ",  "|" ," cantidad: ", huevos_AAA," huevos" ,  "|","Número de badejas: ",AAA ,"(x12 UND)","\n", 
          "Huevos Tipo: BC " ,  "|" ," cantidad: ", huevos_BC, " huevos" ,  "|","Número de badejas: ",BC,"(x30 UND)","\n", 
          )
    print()
    print("--------------------------------------------------------------------------------------")
    print("Total Huevos: ", totalhuevos)
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------")
'''    

#Programa principal 

menuPrincipal()    

#Selección opciones del Menú 

while True:
    try:
        opcion=int(input("Digite una opción: "))
        break
    except ValueError:
        print("Debe digitar las opciones relacionadas en el menú")
        print()

#Ingreso Peso de Huevos Manualmente
    
if opcion==1:      
    while True:
        try:
            cantidadHuevos=int(input("Ingrese la cantidad de huevos a registrar: ")) 
            break
        except ValueError:
            print("Error! el dato debe ser entero. Intenta de nuevo...")
        
    for cantidad in range(cantidadHuevos):    
        while True:
            try:
                peso=float(input(f'Ingrese el peso del huevo número {cantidad+1}: '))
                huevos.append(peso) 
                ordenamiento_burbuja(huevos)
                break
            except ValueError:
                print("Error! debe ingresar un dato numérico. Intenta de nuevo...")
    
clasificacionHuevos(huevos)


#Ingreso Peso de Huevos por Archivo
if opcion==2:
    limpiarPantalla()
    leerArchivo()

#Ingreso Peso de Huevos Aleatoriamente

if opcion==3:
    
    limpiarPantalla()

    while True:
        try:
            cantidadHuevos=int(input("Ingrese la cantidad de huevos que quiere calcular aleatoriamente: ")) 
            break
        except ValueError:
            print("Debe ingresar un dato numérico")
        
    for cantidad in range(cantidadHuevos):    
        while True:
            try:
                peso=random.uniform(10,100)
                huevos.append(peso) 
                ordenamiento_burbuja(huevos)
                break
            except ValueError:
                print("Debe ingresar un dato numérico")
    
clasificacionHuevos(huevos)   
    
                  
if opcion==4:
    limpiarPantalla()
    print("¡Finalizó el Programa!")
    
if opcion>4:
    limpiarPantalla()
    print()
    print("Debe ingresar una de las opciones relacionadas en el menú")
    print("¡Finalizó el Programa!")