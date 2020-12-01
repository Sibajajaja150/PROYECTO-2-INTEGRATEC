#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
###################INTERFAZ GRAFICA###################
#VENTANA DEL PROGRAMA
ventana = Tk() # crea una ventana
ventana.title("ventana integratec")#titulo de la ventana
ventana.geometry("900x800")#tamaño de la ventana
ventana.resizable(True, True)#opcionde modifacar el tamaño
#PANEL 
panel = Frame(ventana, bg='blue', width = 900, height = 800)#crea un panel dentro de la ventana donde se va a trabajar
panel.place(x=0, y=0)#tamaño del panel
#TEXTOS(LABELS)
labelTitulo = Label(panel, text = "MENU INTEGRATEC", bg ='blue', fg = 'white',font = ('',25))#primer label con el titulo en el panel
labelTitulo.place(x=300,y=50)
#TEXTOS(LABELS)
labelNumero = Label(panel, text = "ELIGE UNA OPCION PARA LLEVAR A CABO! ", bg = 'blue', fg = 'white',font = ('',15))#otro label con texto de opciones
labelNumero.place(x=250, y=100)
#BOTONES
boton1 = Button(panel,text = '1)ESTUDIANTE POR SEDE',width=30, height = 2).place(x=350,y=150)
boton2 = Button(panel,text = '2)ESTUDIANTES DE CARRERA POR SEDE',width=30, height = 2).place(x=350,y=200)
boton3 = Button(panel,text = '3)CREAR MENTORES',width=30, height = 2).place(x=350,y=250)
boton4 = Button(panel,text = '4)ASIGNAR MENTORES',width=30, height = 2).place(x=350,y=300)
boton5 = Button(panel,text = '5)ACTUALIZAR ESTUDIANTE',width=30, height = 2).place(x=350,y=350)
boton6 = Button(panel,text = '6)GENERAR REPORTE',width=30, height = 2).place(x=350,y=400)
boton7 = Button(panel,text = '7)CREAR BASE DE DATOS EN EXCEL',width=30, height = 2).place(x=350,y=450)
boton8 = Button(panel,text = '8)ENVIAR CORREO',width=30, height = 2).place(x=350,y=500)
boton9 = Button(panel,text = '9)SALIR',width=30, height = 2).place(x=350,y=550)

ventana.mainloop()#LLAMADA PRINCIPAL