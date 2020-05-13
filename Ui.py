# Interfaz grafica con Tkinter
import csv
import datetime
from tkinter import *
def funcion():
    print ("Excelente")
def resultado():
    abrir_ventana=Toplevel(root)
    abrir_ventana.geometry("205x100")
    root.iconify()
def calculo():
    archivo=open("CalculoCoronavirus.csv")
    reader = csv.reader(archivo,delimiter=';')
    i=0
    acumulador=0
    contador=0
    #creamos una variable min para guardar lo que actualmente esta en aux
    minimo=4
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
        #indicamos el para hallar con el numero mas pequenho despues de 1.0
        contador+=1
        if(aux<=minimo and aux>1.0):
            acumulador=aux
            minimo=aux
root=Tk()
root.geometry("205x100")
titulo1=Label(root,text="Bienvenidos a la calculadora de casos")
titulo1.grid(row=1,column=1)
titulo2=Label(root,text="Ingrese los dias por favor")
titulo2.grid(row=2,column=1)
#creacion basica de etiquetas
boton=Button(root,text="imprimir excelente",command=lambda: print(texto.get()),width=15,height=1,anchor="center")
boton.grid(row=4,column=1)
boton2=Button(root,text="Prueba",command=resultado)
boton2.grid(row=5,column=1)
# boton.place(x=50,y=70)
#creacion basica de botones
texto=Entry(root,justify=CENTER)
texto.grid(row=3,column=1)
root.mainloop()
