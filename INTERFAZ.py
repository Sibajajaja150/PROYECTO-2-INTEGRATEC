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
def volverMenu():
    ventana.mainloop()
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
    botonSalir = Button(panel1,text = 'VOLVER AL MENU',width=30, height = 2, command = volverMenu)
    botonSalir.place(x=150,y=350)
    botonGuardar = Button(panel1,text = 'GUARDAR',width=30, height = 2, command = estudiantesPorSede(eval(inputCTCC),eval(inputCTSC),eval(inputCTSJ),eval(inputCAA),eval(inputCAL)))
    botonGuardar.place(x=150,y=400)
def boton2():
    panel2 = Frame(panel,bg='RoyalBlue3', width = 900, height = 800)
    panel2.place(x=0, y=0)
    labelTitulo2 = Label(panel2, text = "ESTUDIANTES  DE CARRERA POR SEDE", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo2.place(x=80,y=25)
    boton = Button(panel2,text = 'GENERAR ESTUDIANTES DE CARRERA POR SEDE',width=50, height = 2, command = 'FALTA ESTA FUNCION')
    boton.place(x=80,y=100)
    botonSalir = Button(panel2,text = 'VOLVER AL MENU',width=30, height = 2, command = volverMenu)
    botonSalir.place(x=80,y=150)
def boton3():
    panel3 = Frame(panel,bg='RoyalBlue3', width = 900, height = 800)
    panel3.place(x=0, y=0)
    labelTitulo3 = Label(panel3, text = "CREAR MENTORES", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo3.place(x=80,y=25)
    boton = Button(panel3,text = 'GENERAR LOS MENTORES',width=40, height = 2, command = 'FALTA ESTA FUNCION')
    boton.place(x=80,y=100)
    botonSalir = Button(panel3,text = 'VOLVER AL MENU',width=30, height = 2, command = volverMenu)
    botonSalir.place(x=80,y=150)
def boton4():
    panel4 = Frame(panel,bg='RoyalBlue3', width = 900, height = 800)
    panel4.place(x=0, y=0)
    labelTitulo4 = Label(panel4, text = "ASIGNAR MENTORES", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo4.place(x=80,y=25)
    boton = Button(panel4,text = 'ASIGNAR',width=30, height = 2, command = 'FALTA ESTA FUNCION')
    boton.place(x=80,y=100)
    botonSalir = Button(panel4,text = 'VOLVER AL MENU',width=30, height = 2, command = volverMenu)
    botonSalir.place(x=80,y=150)
def boton5():
    panel5 = Frame(panel,bg='RoyalBlue3', width = 900, height = 800)
    panel5.place(x=0, y=0)
    labelTitulo5 = Label(panel5, text = "ACTUALIZAR ESTUDIANTE", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo5.place(x=80,y=25)
    carne = Label(panel5, text = 'CARNE DEL ESTUDIANTE:', bg = 'snow', fg = 'gray10', font = ('',15))
    carne.place(x=80,y=300)
    inputCarne = Text(panel5, width = 30, height = 2)
    inputCarne.place(x = 80, y = 100)
    botonSalir = Button(panel5,text = 'VOLVER AL MENU',width=30, height = 2, command = volverMenu)
    botonSalir.place(x=80,y=150)
#BOTONES DEL MENU PRINCIPAL
boton1 = Button(panel,text = '1)ESTUDIANTE POR SEDE',width=30, height = 2, command = boton1).place(x=350,y=150)
boton2 = Button(panel,text = '2)ESTUDIANTES DE CARRERA POR SEDE',width=30, height = 2, command = boton2).place(x=350,y=200)
boton3 = Button(panel,text = '3)CREAR MENTORES',width=30, height = 2,command = boton3).place(x=350,y=250)
boton4 = Button(panel,text = '4)ASIGNAR MENTORES',width=30, height = 2,command = boton4).place(x=350,y=300)
boton5 = Button(panel,text = '5)ACTUALIZAR ESTUDIANTE',width=30, height = 2,command = boton5).place(x=350,y=350)
boton6 = Button(panel,text = '6)GENERAR REPORTE',width=30, height = 2).place(x=350,y=400)
boton7 = Button(panel,text = '7)CREAR BASE DE DATOS EN EXCEL',width=30, height = 2).place(x=350,y=450)
boton8 = Button(panel,text = '8)ENVIAR CORREO',width=30, height = 2).place(x=350,y=500)
boton9 = Button(panel,text = '9)SALIR',width=30, height = 2).place(x=350,y=550)

ventana.mainloop()#LLAMADA PRINCIPAL