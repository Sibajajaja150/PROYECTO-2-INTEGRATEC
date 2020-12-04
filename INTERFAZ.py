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
#FUNCIONES VARIAS
def validNum(num):
    '''
    funciones: valida un numero de entrada
    e:numero
    s:messagebox
    '''
    try:
        int(num)
    except:
        tkinter.messagebox.showerror('debe insertar solo enteros!')
#def habilitarBotones()
#FUNCIONES DE CADA BOTON
def boton1():
    '''
    funcion: crea una nueva ventana para el reto 1
    e:
    s: una ventana 
    '''
    ventana1 = Tk() # crea una ventana
    ventana1.title("ventana reto 1")#titulo de la ventana
    ventana1.geometry("900x800")#tamaño de la ventana
    ventana1.resizable(True, True)#opcionde modifacar el tamaño
    panel1 = Frame(ventana1, bg='RoyalBlue3', width = 900, height = 800)
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
    inputCTCC = Text(panel1, width = 30, height = 2)#pone un cuadro de texto donde se pueda escrbir
    inputCTCC.place(x = 150, y = 100)
    inputCTSC = Text(panel1, width = 30, height = 2)
    inputCTSC.place(x = 150, y = 150)
    inputCTSJ = Text(panel1, width = 30, height = 2)
    inputCTSJ.place(x = 150, y = 200)
    inputCAA = Text(panel1, width = 30, height = 2)
    inputCAA.place(x = 150, y = 250)
    inputCAL = Text(panel1, width = 30, height = 2)
    inputCAL.place(x = 150, y = 300)
    botonGuardar = Button(panel1,text = 'GUARDAR',width=30, height = 2, command = validarEstudiantesPorSede(inputCTCC,inputCTSC,inputCTSJ,inputCAA,inputCAL))
    botonGuardar.place(x=150,y=400)
    return ''
def boton2():
    '''
    FALTA LA FUNCION: ESTUDIANTES DE CARRERA POR SEDE
    '''
def boton3():
    '''
    FALTA LA FUNCION: CREAR MENTORES
    '''
def boton4():
    '''
    FALTA LA FUNCION: FALTA LA FUNCION:
    '''
def boton5():
    '''
    funcion: crear una nueva ventana para el efectuar el reto 5
    e:
    s: una ventana
    '''
    ventana5 = Tk() # crea una ventana
    ventana5.title("ventana reto 5")#titulo de la ventana
    ventana5.geometry("900x800")#tamaño de la ventana
    ventana5.resizable(True, True)#opcionde modifacar el tamaño
    panel5 = Frame(ventana5, bg='RoyalBlue3', width = 900, height = 800)
    panel5.place(x=0, y=0)
    labelTitulo5 = Label(panel5, text = "ACTUALIZAR ESTUDIANTE", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo5.place(x=80,y=25)
    carne = Label(panel5, text = 'CARNE DEL ESTUDIANTE:', bg = 'snow', fg = 'gray10', font = ('',15))
    carne.place(x=80,y=100)
    inputCarne = Text(panel5, width = 30, height = 2)
    inputCarne.place(x = 350, y = 100)
    return ''
def boton6():
    ventana6 = Tk() # crea una ventana
    ventana6.title("ventana reto 6")#titulo de la ventana
    ventana6.geometry("900x800")#tamaño de la ventana
    ventana6.resizable(True, True)#opcionde modifacar el tamaño
    panel6 = Frame(ventana6,bg='RoyalBlue3', width = 900, height = 800)
    panel6.place(x=0, y=0)
    labelTitulo5 = Label(panel6, text = "GENERAR REPORTES", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo5.place(x=325,y=25)
    botonReporteSede = Button(panel6,text = '1)REPORTE POR SEDE',width=30, height = 2, command = 'FALTA FUNCION').place(x=350,y=150)
    botonReporteCarrera = Button(panel6,text = '1)REPORTE POR CARRERA',width=30, height = 2, command = 'FALTA FUNCION').place(x=350,y=200)
    botonReporteMentor = Button(panel6,text = '1)REPORTE POR MENTOR',width=30, height = 2, command = 'FALTA FUNCION').place(x=350,y=250)
    return ''
def boton7():
    '''
    FALTA FUNCION CREAR DATOS EXCEL
    '''
def boton8():
    ventana8 = Tk() # crea una ventana
    ventana8.title("ventana reto 8")#titulo de la ventana
    ventana8.geometry("900x800")#tamaño de la ventana
    ventana8.resizable(True, True)#opcionde modifacar el tamaño
    panel8 = Frame(ventana8,bg='RoyalBlue3', width = 900, height = 800)
    panel8.place(x=0, y=0)
    labelTitulo8 = Label(panel8, text = "ENVIAR CORREO", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo8.place(x=80,y=25)
    inputCorreo = Text(panel8, width = 30, height = 2)
    inputCorreo.place(x = 150, y = 100)
    tituloInput = Label(panel8, text = 'INSERTE EL CORREO RECEPTOR', bg = 'snow', fg = 'gray10', font = ('',15))
    tituloInput.place(x=80,y=100)
    botonSalir = Button(panel8,text = 'VOLVER AL MENU',width=30, height = 2, command = 'volverMenu')
    botonSalir.place(x=80,y=300)
def boton9():
    ventana.destroy()
#BOTONES DEL MENU PRINCIPAL
boton1 = Button(panel,text = '1)ESTUDIANTE POR SEDE',width=30, height = 2, command = boton1).place(x=350,y=150)
boton2 = Button(panel,text = '2)ESTUDIANTES DE CARRERA POR SEDE',width=30, height = 2, command = boton2).place(x=350,y=200)
boton3 = Button(panel,text = '3)CREAR MENTORES',width=30, height = 2,command = boton3).place(x=350,y=250)
boton4 = Button(panel,text = '4)ASIGNAR MENTORES',width=30, height = 2,command = boton4).place(x=350,y=300)
boton5 = Button(panel,text = '5)ACTUALIZAR ESTUDIANTE',width=30, height = 2,command = boton5).place(x=350,y=350)
boton6 = Button(panel,text = '6)GENERAR REPORTE',width=30, height = 2,command = boton6).place(x=350,y=400)
boton7 = Button(panel,text = '7)CREAR BASE DE DATOS EN EXCEL',width=30, height = 2,command = boton7).place(x=350,y=450)
boton8 = Button(panel,text = '8)ENVIAR CORREO',width=30, height = 2, command = boton8).place(x=350,y=500)
boton9 = Button(panel,text = '9)SALIR',width=30, height = 2,command = boton9).place(x=350,y=550)

ventana.mainloop() #LLAMADA PRINCIPAL
