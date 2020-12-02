#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
from MAINPR2 import *
###################INTERFAZ GRAFICA###################
#VENTANA DEL PROGRAMA
ventana = Tk() # crea una ventana
ventana.title("ventana integratec")#titulo de la ventana
ventana.geometry("900x800")#tamaño de la ventana
ventana.resizable(True, True)#opcionde modifacar el tamaño
#PANEL 
panel = Frame(ventana, bg='RoyalBlue3', width = 900, height = 800)#crea un panel dentro de la ventana donde se va a trabajar
panel.place(x=0, y=0)#tamaño del panel
#TEXTOS(LABELS)
labelTitulo = Label(panel, text = "MENU INTEGRATEC", bg ='snow', fg = 'gray10',font = ('',25))#primer label con el titulo en el panel
labelTitulo.place(x=300,y=50)
#TEXTOS(LABELS)
labelNumero = Label(panel, text = "ELIGE UNA OPCION PARA LLEVAR A CABO! ", bg = 'snow', fg = 'gray10',font = ('',15))#otro label con texto de opciones
labelNumero.place(x=250, y=100)
#FUNCIONES DE CADA BOTON
def boton1():
    panel1 = Frame(panel, bg='RoyalBlue3', width = 900, height = 800)
    panel1.place(x=0, y=0)
    labelTitulo1 = Label(panel1, text = "ESTUDIANTES POR SEDE", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo1.place(x=300,y=25)
    ctcc = Label(panel1, text = 'CTCC', bg = 'snow', fg = 'gray10', font = ('',15))
    ctcc.place(x=80,y=100)
    ctsc = Label(panel1, text = 'CTSC', bg = 'snow', fg = 'gray10', font = ('',15))
    ctsc.place(x=80,y=150)
    ctsj = Label(panel1, text = 'CTSJ', bg = 'snow', fg = 'gray10', font = ('',15))
    ctsj.place(x=80,y=200)
    caa = Label(panel1, text = 'CAA', bg = 'snow', fg = 'gray10', font = ('',15))
    caa.place(x=80,y=250)
    cal = Label(panel1, text = 'CAL', bg = 'snow', fg = 'gray10', font = ('',15))
    cal.place(x=80,y=300)
    inputCTCC = Text(panel, width = 30, height = 2)#pone un cuadro de texto donde se pueda escrbir
    inputCTCC.place(x = 150, y = 100)
    inputCTSC = Text(panel, width = 30, height = 2)
    inputCTSC.place(x = 150, y = 150)
    inputCTSJ = Text(panel, width = 30, height = 2)
    inputCTSJ.place(x = 150, y = 200)
    inputCAA = Text(panel, width = 30, height = 2)
    inputCAA.place(x = 150, y = 250)
    inputCAL = Text(panel, width = 30, height = 2)
    inputCAL.place(x = 150, y = 300)
    estudiantesPorSede(inputCTCC,inputCTSC,inputCTSJ,inputCAA,inputCAL)
def boton2():
    return''
#BOTONES
boton1 = Button(panel,text = '1)ESTUDIANTE POR SEDE',width=30, height = 2, command = boton1).place(x=350,y=150)
boton2 = Button(panel,text = '2)ESTUDIANTES DE CARRERA POR SEDE',width=30, height = 2).place(x=350,y=200)
boton3 = Button(panel,text = '3)CREAR MENTORES',width=30, height = 2).place(x=350,y=250)
boton4 = Button(panel,text = '4)ASIGNAR MENTORES',width=30, height = 2).place(x=350,y=300)
boton5 = Button(panel,text = '5)ACTUALIZAR ESTUDIANTE',width=30, height = 2).place(x=350,y=350)
boton6 = Button(panel,text = '6)GENERAR REPORTE',width=30, height = 2).place(x=350,y=400)
boton7 = Button(panel,text = '7)CREAR BASE DE DATOS EN EXCEL',width=30, height = 2).place(x=350,y=450)
boton8 = Button(panel,text = '8)ENVIAR CORREO',width=30, height = 2).place(x=350,y=500)
boton9 = Button(panel,text = '9)SALIR',width=30, height = 2).place(x=350,y=550)

ventana.mainloop()#LLAMADA PRINCIPAL