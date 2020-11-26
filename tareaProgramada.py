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
url = "https://www.tec.ac.cr/carreras"
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
def crearListaSJ(lista):
    listaSJ = []
    for i in lista[1:]:
        if i.upper() == "CAMPUS TECNOLÓGICO CENTRAL CARTAGO":
            break
        else:
            if i not in listaSJ:
                listaSJ += [i]
    diccSJ = {}
    for i in listaSJ:
        diccSJ [i] = 0
    return [diccSJ]
def crearListaC (lista):
    listaC = []
    for i in lista[8:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaC:
                listaC += [i]
    diccC = {}
    for i in listaC:
        diccC [i] = 0
    return [diccC]
#print(lista[68:])
def crearListaSC(lista):
    listaSC = []
    for i in lista[48:]:
        if i.upper() == "CENTRO ACADÉMICO DE LIMÓN":
            break
        else:
            if i not in listaSC:
                listaSC += [i]
    diccSC = {}
    for i in listaSC:
        diccSC [i] = 0
    return [diccSC]
def crearListaL(lista):
    listaL = []
    for i in lista[61:]:
        if i.upper() == "CENTRO ACADÉMICO DE ALAJUELA":
            break
        else:
            if i not in listaL:
                listaL += [i]
    diccL = {}
    for i in listaL:
        diccL [i] = 0
    return [diccL]
def crearListaA(lista):
    listaA = []
    for i in lista[68:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaA:
                listaA += [i]
    diccA = {}
    for i in listaA:
        diccA [i] = 0
    return [diccA]
matrizDicc = [["CTCC", crearListaC(lista)],["CTLSC", crearListaSC(lista)],["CTLSJ", crearListaSJ(lista)],["CAA", crearListaA(lista)],["CAL", crearListaL(lista)]]
print(matrizDicc)