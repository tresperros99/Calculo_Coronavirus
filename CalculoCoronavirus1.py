#!/usr/bin/env python
#Programa para predecir futuros casos de coronavirus en el paraguay
import csv
#importamos la libreria datetima para poder trabajar con fechas
import datetime
import tkinter
archivo=open("CalculoCoronavirus.csv")
reader = csv.reader(archivo,delimiter=';')
i=0
acumulador=0
contador=0
for linea in reader:
    #usamos esta condicion para poder obtener a partir de la segunda fila del csv y asi evitar el conflicto por tipos de datos
    if i==0:
        i+=1
        continue
    #usamos la variable caso para saber el valor de la cantidad de casos del ultimo dia registrado
    caso=linea[1]
    #usamos la variable fecha por la misma rason que caso
    fecha=linea[0]
    #usamos un condicionante para romper el ciclo si es que los datos en esa celda valen 0
    if(linea[2]=='0'):
        break
    aux=(linea[2])
    aux=float(aux)
    acumulador=acumulador+aux
    contador+=1

promedio=acumulador/contador
print("A continuacion se presenta un pequenho programa que su funcion principal es tratar de predecir por medio de calculos estadisticos")
print("la cantidad de casos de coronavirus en los siguientes dias en nuestro Paraguay")
print("----------------------------------------------------------------------------------")
print("El funcionamiento es simple, solo usted tiene que ingresar la cantidad de dias que usted desea saber los casos probables de dicho dia")
print("contando desde hoy obviamente  ")
print("----------------------------------------------------------------------------------")
print("La fecha actual es",datetime.datetime.utcnow())
print("----------------------------------------------------------------------------------")
dias=int(input("Por favor ingrese los dias:"))
caso=int(caso)
contador_casos=0
for e in range(0,dias):
    contador_casos=contador_casos+(caso*promedio)

print("La cantidad de casos confirmados en", dias,"dias probablemente sera:",int(contador_casos),"casos")
input() 