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
listaCE = []
matrizSede = []
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
    matrizDicc = [["CTCC", asignarE(crearListaC(lista)[:10], a)],["CTLSC", asignarE(crearListaSC(lista), b)],["CTLSJ", asignarE(crearListaSJ(lista), c)],["CAA", asignarE(crearListaA(lista), d)],["CAL", asignarE(crearListaL(lista), e)]]
    return matrizDicc
def isNum(string):
    try:
        return type(eval(string)) == int
    except:
        return False
def validarEstudiantesPorSede(a,b,c,d,e):
    global matrizSede
    if isNum(a) and isNum(b) and isNum(c) and isNum(d) and isNum(e):
        matrizSede = estudiantesPorSede(int(a), int(b), int(c), int(d), int(e))
        return estudiantesPorSede(int(a), int(b), int(c), int(d), int(e))
    else:
        print("Ingrese un numero valido")
def crearListaCarreras(lista):
    listaN = [] 
    k = lista[1].keys()
    for x in k:
        listaN += [x]
    return listaN
def crearListaEstudiantes(lista):
    listaN = [] 
    k = lista[1].values()
    for x in k:
        listaN += [x]
    return listaN
def crearLista(lista1, lista2):
    listaF = []
    for i in lista1:
        listaF += [[i, lista2[0]]]
        lista2.pop(0)
    return listaF
def listaEstudiantes(lista):
    listaN = []
    contador = 0
    for i in lista:
        for j in i[1]:
            if j[1] > 0:
                x = j[1]
                while x != 0:
                    numeros = ["8", "6" , "7" , "9"]
                    listaN += [["20210" + str(contador) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), names.get_first_name() + " " + names.get_last_name() + " " + names.get_last_name(), numeros[random.randint(0, 3)] + str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9)), i[0], j[0], 0, ""]]
                    x -= 1
        contador += 1
    return listaN
def makeDicc(lista):
    dicc = {}
    for i in lista:
        dicc[i[0]] = i[1:]
    return dicc
def enviarCorreos(correo):
    mensaje = MIMEMultipart ("plain")
    mensaje["From"] = "diegoesteban42069@gmail.com"
    usuario = correo
    mensaje["To"] = usuario
    mensaje["Subject"] = "Prueba"
    adjunto = MIMEBase("application", "octect-stream")
    adjunto.set_payload(open("hola.txt", "rb").read())
    adjunto.add_header("content-Disposition", "attachment; filename = 'Mensaje.txt'")
    mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("diegoesteban42069@gmail.com", "420696969")
    smtp.sendmail("diegoesteban42069@gmail.com", usuario, mensaje.as_string())
    smtp.quit()
dicc=makeDicc(listaEstudiantes(listaCE))
def actualizarEstudiante(carnet, nombre, telefono, correo, dicc):
    dicc[carnet][0] = nombre
    dicc[carnet][1] = telefono
    dicc[carnet][5] = correo
    print(dicc[carnet])
    return ""
validarEstudiantesPorSede('2', '4', '5', '3', '3')
listaCE = [["CTCC", crearLista(crearListaCarreras(matrizSede[0]), crearListaEstudiantes(matrizSede[0]))], ["CTLSC", crearLista(crearListaCarreras(matrizSede[1]), crearListaEstudiantes(matrizSede[1]))], ["CTLSJ", crearLista(crearListaCarreras(matrizSede[2]), crearListaEstudiantes(matrizSede[2]))], ["CAA", crearLista(crearListaCarreras(matrizSede[3]), crearListaEstudiantes(matrizSede[3]))], ["CAL", crearLista(crearListaCarreras(matrizSede[4]), crearListaEstudiantes(matrizSede[4]))]]
#print(listaCE)
#diccEstudiantes = {listaCE[0][0]:listaCE[0][1], listaCE[1][0]:listaCE[1][1], listaCE[2][0]:listaCE[2][1], listaCE[3][0]:listaCE[3][1], listaCE[4][0]:listaCE[4][1]}
h = listaEstudiantes(listaCE)
<<<<<<< Updated upstream
print(h)
print(makeDicc(h))
def buscarSede(nombre, lista):
    for i in lista:
        if i[0] == nombre.upper():
            return i
    print("No existe la sede")
    return ""
def crearHTMLSede():
    print ()
=======
#print(h)
>>>>>>> Stashed changes
