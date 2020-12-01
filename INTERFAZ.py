#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#importacion  de librerias
import tkinter
from tkinter import *
import pip
from pip import *
from 
###################INTERFAZ GRAFICA###################
ventana = Tk() # crea una ventana
ventana.title("ventana principal")
ventana.geometry("900x800")
ventana.resizable(FALSE, FALSE)
imagenIntegratec = ImageTK.PhotoImage(Image.open(r'C:\Users\esteb\OneDrive\Imágenes\TEC\integratec.png'))
image1 = Image.tk.PhotoImage(imagenIntegratec)
w = image1.width()
h = image1.height()
ventana.geometry('%dx%d+0+0' % (w,h))
labelText = StringVar()
labelText.set("Welcome !!!!")
label1 = Label(ventana, image=image1, textvariable=labelText,
                  font=("Times New Roman", 24),
                  justify=CENTER, height=4, fg="blue")
label1.pack()
panel = Frame(ventana, bg='blue', width = 900, height = 800)
panel.place(x=0, y=0)
ventana.mainloop() 