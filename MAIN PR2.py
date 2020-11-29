#Elaborado por : Diego Vega y Esteba Sibaja
#Fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#IMPORTACION DE LIBRERIAS
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import requests
import names
import random
from datetime import time
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
    return listaSJ
def crearListaC (lista):
    listaC = []
    for i in lista[8:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaC:
                listaC += [i]
    return listaC
#print(lista[68:])
def crearListaSC(lista):
    listaSC = []
    for i in lista[48:]:
        if i.upper() == "CENTRO ACADÉMICO DE LIMÓN":
            break
        else:
            if i not in listaSC:
                listaSC += [i]
    return listaSC
def crearListaL(lista):
    listaL = []
    for i in lista[61:]:
        if i.upper() == "CENTRO ACADÉMICO DE ALAJUELA":
            break
        else:
            if i not in listaL:
                listaL += [i]
    return listaL
def crearListaA(lista):
    listaA = []
    for i in lista[68:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaA:
                listaA += [i]
    return listaA
def crearListaR(n, lista):
    listaR = []
    while len(listaR) != len(lista):
        listaR += [random.randint(0,n)]
    return listaR
def sumaLista(lista):
    res = 0
    for i in lista:
        res += i
    return res        
def crearListaRes(n, lista):
    res = ""
    while n != res:
        i = crearListaR(n, lista)
        res = sumaLista(i)
    return i
def asignarE(lista, num):
    dicc = {}
    listaR = crearListaRes(num, lista)
    n = 0
    for i in lista:
        dicc[i] = listaR[n]
        n += 1
    return dicc
def estudiantesPorSede(a,b,c,d,e):
    matrizDicc = [["CTCC", asignarE(crearListaC(lista), a)],["CTLSC", asignarE(crearListaSC(lista), b)],["CTLSJ", asignarE(crearListaSJ(lista), c)],["CAA", asignarE(crearListaA(lista), d)],["CAL", asignarE(crearListaL(lista), e)]]
    return matrizDicc
def isNum(string):
    try:
        return type(eval(string)) == int
    except:
        return False
def validarEstudiantesPorSede(a,b,c,d,e):
    if isNum(a) and isNum(b) and isNum(c) and isNum(d) and isNum(e):
        return estudiantesPorSede(int(a), int(b), int(c), int(d), int(e))
    else:
        print("Ingrese un numero valido")
def estudiantesPorSedeUsuario():
    a =input("Ingrese los estudiantes del Campus Tecnologico Central de Cartago ")
    b = input("Ingrese los estudiantes del Campus Tecnologico Local de San Carlos ")
    c = input("Ingrese los estudiantes del Campus Tecnologico Local de San Jose ")
    d = input("Ingrese los estudiantes del Centro Academico de Alajuela ")
    e = input("Ingrese los estudiantes del Centro Academico de Limon ")
    print(validarEstudiantesPorSede(a,b,c,d,e))
    return ""
#matrizSede = estudiantesPorSedeUsuario()
#dicc = asignarE(crearListaA(lista), 50)
#estudiantes = dicc.values()
#carreras = dicc.keys()
#print(carreras)
#print(estudiantes)