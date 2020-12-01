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
ventana = Tk() # crea una ventana
ventana.title("ventana integratec")
ventana.geometry("900x800")
ventana.resizable(True, True)

panel = Frame(ventana, bg='blue',width= 900, height=800)#crea un panel con caracterisiticas
panel.place(x=0, y=0) #pocisiona el panel
labelTitulo = Label(panel, text = "MENU INTEGRATEC", bg ='blue', fg = 'white',font = ('',18))#primer label
labelTitulo.place(x=350,y=100)
labelNumero = Label(panel, text = "INGRESE EL NUMERO", bg = 'blue', fg = 'white',font = ('',18))#otro label
labelNumero.place(x=75, y=150)
panel = Frame(ventana, bg='gray18', width = 900, height = 800)
panel.place(x=0, y=0)
boton1 = Button(ventana,text = '1)ESTUDIANTE POR SEDE',width=30, height = 2).place(x=350,y=150)
boton2 = Button(ventana,text = '2)ESTUDIANTES DE CARRERA POR SEDE',width=30, height = 2).place(x=350,y=200)
boton3 = Button(ventana,text = '3)CREAR MENTORES',width=30, height = 2).place(x=350,y=250)
boton4 = Button(ventana,text = '4)ASIGNAR MENTORES',width=30, height = 2).place(x=350,y=300)
boton5 = Button(ventana,text = '5)ACTUALIZAR ESTUDIANTE',width=30, height = 2).place(x=350,y=350)
boton6 = Button(ventana,text = '6)GENERAR REPORTE',width=30, height = 2).place(x=350,y=400)
boton7 = Button(ventana,text = '7)CREAR BASE DE DATOS EN EXCEL',width=30, height = 2).place(x=350,y=450)
boton8 = Button(ventana,text = '8)ENVIAR CORREO',width=30, height = 2).place(x=350,y=500)
boton9 = Button(ventana,text = '9)SALIR',width=30, height = 2).place(x=350,y=550)
ventana.mainloop()