# Interfaz grafica con Tkinter
import csv
import datetime
from tkinter import *
def funcion():
    print ("Excelente")
def resultado(contador_casos,dias):
    abrir_ventana=Toplevel(root)
    abrir_ventana.geometry("140x70")
    root.iconify()
    titulo=Label(abrir_ventana,text="Aproximadamente habra")
    titulo.grid(row=1,column=1)
    etiqueta_resultado=Label(abrir_ventana,text=contador_casos,justify=CENTER)
    etiqueta_resultado.grid(row=2,column=1)
    dias=str(dias)
    texto="Casos en "+dias+" dias"
    abajo=Label(abrir_ventana,text=texto,)
    abajo.grid(row=3,column=1)
    etiqueta_resultado.mainloop()
def calculo():
    #primeramente guardamos en dias la variable obtenida
    dias=var_entrada.get()
    print(dias)
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
    caso=int(caso)
    contador_casos=0
    #la varianter con respecto a la version anterior es que en vez de multiplicar por un promedio
    #se multiplica por el numero mas chico mayor que 1.0
    for e in range(0,dias):
        contador_casos=contador_casos+(caso*acumulador)
    contador_casos=int(contador_casos)
    resultado(contador_casos,dias)
    
        
root=Tk()
root.geometry("205x100")
titulo1=Label(root,text="Bienvenidos a la calculadora de casos")
titulo1.grid(row=1,column=1)
titulo2=Label(root,text="Ingrese los dias por favor")
titulo2.grid(row=2,column=1)
#creacion basica de etiquetas
#creacion de la variable para guardar las cosas
var_entrada=IntVar()
texto=Entry(root,justify=CENTER,textvariable=var_entrada)
texto.grid(row=3,column=1)
boton=Button(root,text="Go",command=calculo,width=15,height=1,anchor="center")
boton.grid(row=4,column=1)
#creacion basica de botones
root.mainloop()
