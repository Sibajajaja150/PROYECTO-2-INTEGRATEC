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
ventana.title("ventana principal")
ventana.iconbitmap(r'C:\Users\esteb\OneDrive\Imágenes\TEC\iconoPython.png')
ventana.geometry("900x800")
ventana.resizable(FALSE, FALSE)
panel = Frame(ventana, bg='gray18', width = 900, height = 800)
panel.place(x=0, y=0)
ventana.mainloop() 