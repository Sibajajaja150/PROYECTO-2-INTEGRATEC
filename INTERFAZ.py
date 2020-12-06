#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: 5/12/2020 11:05pm
#version: 3.8.6
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
from MAINPR2 import *
from ARCHIVOS import *
###################INTERFAZ GRAFICA###################
#variables globales
a = []
b = []
c = []
listaGlobal = []
#VENTANA DEL PROGRAMA
ventana = Tk() # crea una ventana
ventana.title("ventana integratec")#titulo de la ventana
ventana.geometry("900x800")#tamaño de la ventana
ventana.resizable(True, True)#opcionde modifacar el tamaño
#PANEL PRINCIPAL
panel = Frame(ventana, bg='RoyalBlue3', width = 900, height = 800)#crea un panel dentro de la ventana donde se va a trabajar
panel.place(x=0, y=0)#tamaño del panel
#TEXTOS(LABELS)
labelTitulo = Label(panel, text = "menu integratec", bg ='snow', fg = 'gray10',font = ('',25))#primer label con el titulo en el panel
labelTitulo.place(x=300,y=50)
#TEXTOS(LABELS)
labelNumero = Label(panel, text = "elige una opcion para llevar a cabo! ", bg = 'snow', fg = 'gray10',font = ('',15))#otro label con texto de opciones
labelNumero.place(x=250, y=100)
#FUNCIONES VARIAS
def listaCEAux(dicc):
    '''
    funcion: crea una lista auxiliar
    e: diccionario
    s:
    '''
    global listaGlobal
    print(dicc)
    listaGlobal = listaCE(dicc)
    return ""
def validNum(num):
    '''
    funciones: valida un numero de entrada
    e:numero
    s:messagebox
    '''
    try:
        int(num)
    except:
        tkinter.messagebox.showerror('mensaje','debe insertar solo enteros!')
    return''
def habilitarBotones(matrizCarrerasSede,estudiantes,mentores):
    '''
    funcion: hablilitar y deshabilitar botones
    e: 3 dicc
    s:
    '''
    matrizCarrerasSede = existeArch(estudiantes,getCorreo(listaEstudiantes(listaCE)))
    mentores = existeArch(getCorreo(listaMentores(listaCE)))
    if matrizCarrerasSede == []:
        boton2['state']=tkinter.DISABLED
        boton3['state']=tkinter.DISABLED
    else:
        boton2['state']=tkinter.NORMAL
        boton3['state']=tkinter.NORMAL
    if mentores == []:
        boton4['state']=tkinter.DISABLED
    else:
        boton4['state']=tkinter.NORMAL
    if estudiantes == []:
        boton5['state']=tkinter.DISABLED
    else:
        boton5['state']=tkinter.NORMAL
    return ''
#FUNCIONES DE CADA BOTON
def retornarMatrisSede(valor):
    '''
    funcion: retornar una matriz 
    e: un valor
    s: una matriz 
    '''
    return valor
def boton1():
    '''
    funcion: crea una nueva ventana para el reto 1
    e:
    s: una ventana 
    '''
    global matrizSede
    global listaGlobal
    ventana1 = Tk() # crea una ventana
    ventana1.title("ventana reto 1")#titulo de la ventana
    ventana1.geometry("900x800")#tamaño de la ventana
    ventana1.resizable(True, True)#opcionde modifacar el tamaño
    panel1 = Frame(ventana1, bg='RoyalBlue3', width = 900, height = 800)
    panel1.place(x=0, y=0)
    labelTitulo1 = Label(panel1, text = "estudiantes por sede", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo1.place(x=150,y=50)
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
    inputCTCC = Entry(panel1)#pone un cuadro de texto donde se pueda escrbir
    inputCTCC.place(x = 150, y = 100)
    inputCTSC = Entry(panel1)
    inputCTSC.place(x = 150, y = 150)
    inputCTSJ = Entry(panel1)
    inputCTSJ.place(x = 150, y = 200)
    inputCAA = Entry(panel1)
    inputCAA.place(x = 150, y = 250)
    inputCAL = Entry(panel1)
    inputCAL.place(x = 150, y = 300)
    botonGuardar = Button(panel1,text = 'guardar',width=30, height = 2, command = lambda: listaCEAux(validarEstudiantesPorSede(inputCTCC.get(),inputCTSC.get(),inputCTSJ.get(),inputCAA.get(),inputCAL.get())))
    botonGuardar.place(x=150,y=400)
    #matrizSede = validarEstudiantesPorSede(inputCTCC.get(),inputCTSC.get(),inputCTSJ.get(),inputCAA.get(),inputCAL.get())
    #print(matrizSede)
    return ''
def boton2():
    global listaGlobal
    global a
    '''
    Funcion: crea una lista con los estudiantes
    e:
    s:
    '''
    a = getCorreo(listaEstudiantes(listaGlobal))
    print (a)
    return ''
def boton3():
    global listaGlobal
    global b
    '''
    funcion: crea los mentores
    e:
    s:
    '''
    b = getCorreo(listaMentores(listaGlobal))
    grabar("listaMentores.txt", lista)
    print (b)
    return ''
def boton4():
    global a
    global b
    global c
    '''
    funcion: asigna mentores a cada estudiante
    e:
    s:
    '''
    c = asignarMentores(a, b)
    print ("Mentores asignados con exito")
    return ''
def boton5():
    '''
    funcion: crear una nueva ventana para el efectuar el reto 5
    e:
    s: una ventana
    '''
    global a
    diccionario = makeDicc(a)
    ventana5 = Tk() # crea una ventana
    ventana5.title("ventana reto 5")#titulo de la ventana
    ventana5.geometry("900x800")#tamaño de la ventana
    ventana5.resizable(True, True)#opcionde modifacar el tamaño
    panel5 = Frame(ventana5, bg='RoyalBlue3', width = 900, height = 800)
    panel5.place(x=0, y=0)
    labelTitulo5 = Label(panel5, text = "actualizar estudiante", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo5.place(x=100,y=25)
    carne = Label(panel5, text = 'carne del estudiante:', bg = 'snow', fg = 'gray10', font = ('',15))
    carne.place(x=80,y=100)
    inputCarne = Entry(panel5)
    inputCarne.place(x = 350, y = 100)
    nombre = Label(panel5, text = 'nuevo nombre del estudiante:', bg = 'snow', fg = 'gray10', font = ('',15))
    nombre.place(x=80,y=200)
    inputNombre = Entry(panel5)
    inputNombre.place(x=350,y=200)
    telefono = Label(panel5, text = 'nuevo telefono:', bg = 'snow', fg = 'gray10', font = ('',15))
    telefono.place(x=80,y=300)
    inputTelefono = Entry(panel5)
    inputTelefono.place(x=350,y=300)
    carne = Label(panel5, text = 'nuevo correo:', bg = 'snow', fg = 'gray10', font = ('',15))
    carne.place(x=80,y=400)
    inputCorreo = Entry(panel5)
    inputCorreo.place(x=350,y=400)
    #diccionario = makeDicc(listaEstudiantes(listaCE))
    #print(listaEstudiantes(listaCE))
    #print(diccionario)
    botonBuscar = Button(panel5,text = 'buscar',width=30, height = 2, command = lambda: actualizarEstudiante(inputCarne.get(),inputNombre.get(),inputTelefono.get(),inputCorreo.get(),diccionario))
    botonBuscar.place(x=500,y=100)
    return ''
def reporteCarrera(var1):
    '''
    funcion: crea un frame para ingresar la carrera
    e: una variable
    s:
    '''
    global a
    ventanaCarrera = Tk() # crea una ventana
    ventanaCarrera.title("ventana reto 6")#titulo de la ventana
    ventanaCarrera.geometry("900x800")#tamaño de la ventana
    ventanaCarrera.resizable(True, True)#opcionde modifacar el tamaño
    panelCarrera = Frame(ventanaCarrera,bg='RoyalBlue3', width = 900, height = 800)
    panelCarrera.place(x=0, y=0)
    inputTitulo = Label(panelCarrera,text = 'ingrese la carrera deseada:',bg ='snow', fg = 'gray10',font = ('',15)).place(x=25,y=200)
    inputCarrera = Entry(panelCarrera)
    inputCarrera.place(x=300,y=200)
    def crear(a):
        var = inputCarrera.get()
        return crearHTMLCarrera(a,var)
    labelTituloCarrera = Label(panelCarrera, text = "generar reporte de carreras", bg ='snow', fg = 'gray10',font = ('',20))
    labelTituloCarrera.place(x=325,y=25)
    botonGenerar = Button(panelCarrera,text='generar reporte',width=30,height=2,command = lambda:crear(var1))
    botonGenerar.place(x=300,y=300)
    return ''
def boton6():
    '''
    funcion: corre la funcion del reto 6 y crea una ventana
    e:
    s:
    '''
    global a
    global c
    ventana6 = Tk() # crea una ventana
    ventana6.title("ventana reto 6")#titulo de la ventana
    ventana6.geometry("900x800")#tamaño de la ventana
    ventana6.resizable(True, True)#opcionde modifacar el tamaño
    panel6 = Frame(ventana6,bg='RoyalBlue3', width = 900, height = 800)
    panel6.place(x=0, y=0)
    entradaSede = separarLista(a)
    labelTitulo6 = Label(panel6, text = "generar reportes", bg ='snow', fg = 'gray10',font = ('',20)).place(x=325,y=20)
    botonReporteSede = Button(panel6,text='1)reporte por sede',width=30,height=2,command=lambda:HTMLSede(entradaSede)).place(x=350,y=150)
    botonReporteCarrera = Button(panel6,text='2)reporte por carrera',width=30,height=2,command=lambda:reporteCarrera(a))
    botonReporteCarrera.place(x=350,y=200)
    botonReporteMentor = Button(panel6,text ='3)reporte por mentor',width=30,height=2,command=lambda:crearHTMLMentores(c)).place(x=350,y=250)
    return ''
def boton7():
    '''
    funcion: crea en la base de datos un excel
    e:
    s:
    '''
    crearExcel(a,b)
    return ''
def boton8():
    '''
    funcion: reto 8 enviar correos
    e:
    s:
    '''
    ventana8 = Tk() # crea una ventana
    ventana8.title("ventana reto 8")#titulo de la ventana
    ventana8.geometry("900x800")#tamaño de la ventana
    ventana8.resizable(True, True)#opcionde modifacar el tamaño
    panel8 = Frame(ventana8,bg='RoyalBlue3', width = 900, height = 800)
    panel8.place(x=0, y=0)
    labelTitulo8 = Label(panel8, text = "enviar correo", bg ='snow', fg = 'gray10',font = ('',20))
    labelTitulo8.place(x=80,y=25)
    inputCorreo = Entry(panel8)
    inputCorreo.place(x = 325, y = 100)
    tituloInput = Label(panel8, text = 'inserte el correo receptor', bg = 'snow', fg = 'gray10', font = ('',15))
    tituloInput.place(x=80,y=100)
    botonEnviar = Button(panel8,text = 'enviar',width=30,height=2,command=lambda: enviarCorreos(inputCorreo)).place(x = 325, y = 200)
    return ''
def boton9():
    '''
    funcion: cerrar la ventana principal
    e:
    s:
    '''
    ventana.destroy()
    print('gracias por usar el sistema integratec!')
    return ''
#BOTONES DEL MENU PRINCIPAL
boton1 = Button(panel,text = '1)Estudiante por sede',width=30, height = 2, command = boton1).place(x=350,y=150)
boton2 = Button(panel,text = '2)Estudiantes de carrera por sede',width=30, height = 2, command = boton2).place(x=350,y=200)
boton3 = Button(panel,text = '3)Crear mentores',width=30, height = 2,command = boton3).place(x=350,y=250)
boton4 = Button(panel,text = '4)Asignar mentores',width=30, height = 2,command = boton4).place(x=350,y=300)
boton5 = Button(panel,text = '5)Actualizar estudiante',width=30, height = 2,command = boton5).place(x=350,y=350)
boton6 = Button(panel,text = '6)Generar reportes',width=30, height = 2,command = boton6).place(x=350,y=400)
boton7 = Button(panel,text = '7)Crear base de datos de excel',width=30, height = 2,command = boton7).place(x=350,y=450)
boton8 = Button(panel,text = '8)Enviar correo',width=30, height = 2, command = boton8).place(x=350,y=500)
boton9 = Button(panel,text = '9)Salir',width=30, height = 2,command = boton9).place(x=350,y=550)

ventana.mainloop() #LLAMADA PRINCIPAL

#print(validarEstudiantesPorSede('5','6','8','12','10'))
#listaCE = [["CTCC", crearLista(crearListaCarreras(matrizSede[0]), crearListaEstudiantes(matrizSede[0]))], ["CTLSC", crearLista(crearListaCarreras(matrizSede[1]), crearListaEstudiantes(matrizSede[1]))], ["CTLSJ", crearLista(crearListaCarreras(matrizSede[2]), crearListaEstudiantes(matrizSede[2]))], ["CAA", crearLista(crearListaCarreras(matrizSede[3]), crearListaEstudiantes(matrizSede[3]))], ["CAL", crearLista(crearListaCarreras(matrizSede[4]), crearListaEstudiantes(matrizSede[4]))]]
#ventana.mainloop()
