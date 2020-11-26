#Elaborado por : Diego Vega y Esteba Sibaja
#Fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import requests
import names
import tkinter
url = "https://www.tec.ac.cr/planes-estudio"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
cuadros = soup.find_all ("div", class_ = "group")
info = ""
for i in cuadros:
    info += i.text
info = info.split("\n")
lista = []
for i in info:
    if i != "":
        lista.append(i)
<<<<<<< HEAD

print(lista)
def prueba():
    print('prueba mod 12')
    print('hola')
=======
#def crearMatriz(lista):
>>>>>>> 32751b9bc8ddec052dd9974dce94e7a95e25d357
