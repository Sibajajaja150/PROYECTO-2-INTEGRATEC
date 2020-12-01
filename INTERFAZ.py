#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#importacion  de librerias
import tkinter
from tkinter import *
###################INTERFAZ GRAFICA###################
ventana = Tk() # crea una ventana
ventana.title("ventana principal")
ventana.geometry("1080x1080")
ventana.resizable(FALSE, FALSE)
panel = Frame(ventana, bg='green', width = 1080, height = 1080)
panel.place(x=0, y=0)
ventana.mainloop() 