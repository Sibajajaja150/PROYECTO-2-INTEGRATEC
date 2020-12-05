#Elaborado por : Diego Vega y Esteba Sibaja
#Fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.6
#IMPORTACION DE LIBRERIAS
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import requests
import names
import random
import datetime
import csv 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
archivo = ""
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
        return matrizSede
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
                    listaN += [["20210" + str(contador) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), names.get_first_name() + " " + names.get_last_name() + " " + names.get_last_name(), numeros[random.randint(0, 3)] + str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9))+ str(random.randint(0, 9)), i[0], j[0], "0", ""]]
                    x -= 1
        contador += 1
    return listaN
def makeDicc(lista):
    dicc = {}
    for i in lista:
        dicc[i[0]] = i[1:]
    return dicc
def listaMentores(lista):
    listaN = []
    contador = 0
    for i in lista:
        for j in i[1]:
            if j[1] > 0:
                x = round((j[1]*0.05), 0)
                while int(x) != 0:
                    listaN += [["20210" + str(contador) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)), names.get_first_name() + " " + names.get_last_name() + " " + names.get_last_name(), i[0], j[0], ""]]
                    x -= 1
        contador += 1
    return listaN
def asignarMentores(lista1, lista2):
    listaConjunto = []
    for i in lista1:
        if i[3] == lista2[0][2] and i[4] == lista2[0][3]:
            i[5] = lista2[0][0]
            listaConjunto += [[lista2[0], i]]       
            lista2.pop(0)
        if lista2 == []:
            break
    return listaConjunto
def getNameLastName(nombre):
    listaN = [[""], [""]]
    cont = 0
    for i in nombre:
        if cont == 2:
            break
        if i == " ":
            cont += 1
            continue
        listaN[cont][0] += i
    return listaN
def getCorreo(lista):
    correos = []
    for i in lista:
        contador = 1
        correo =  getNameLastName(i[1])[0][0][:contador] + getNameLastName(i[1])[1][0] + "@estudiantec.cr"
        #while correo not in correos:
            #contador += 1
            #correo =  getNameLastName(i[1])[0][0][:contador] + getNameLastName(i[1])[1][0] + "@estudiantec.cr"
        correos += [correo]
        i[-1] = correo
    return lista
#dicc=makeDicc(listaEstudiantes(listaCE))
def actualizarEstudiante(carnet, nombre, telefono, correo, dicc):
    print(dicc[carnet])
    dicc[carnet][0] = nombre
    dicc[carnet][1] = telefono
    dicc[carnet][5] = correo
    print(dicc[carnet])
    return ""
validarEstudiantesPorSede('2', '4', '11', '18', '25')
listaCE = [["CTCC", crearLista(crearListaCarreras(matrizSede[0]), crearListaEstudiantes(matrizSede[0]))], ["CTLSC", crearLista(crearListaCarreras(matrizSede[1]), crearListaEstudiantes(matrizSede[1]))], ["CTLSJ", crearLista(crearListaCarreras(matrizSede[2]), crearListaEstudiantes(matrizSede[2]))], ["CAA", crearLista(crearListaCarreras(matrizSede[3]), crearListaEstudiantes(matrizSede[3]))], ["CAL", crearLista(crearListaCarreras(matrizSede[4]), crearListaEstudiantes(matrizSede[4]))]]
#print(listaCE)
#diccEstudiantes = {listaCE[0][0]:listaCE[0][1], listaCE[1][0]:listaCE[1][1], listaCE[2][0]:listaCE[2][1], listaCE[3][0]:listaCE[3][1], listaCE[4][0]:listaCE[4][1]}
def separarLista(lista):
    listaN = [["CTCC"], ["CTLSC"], ["CTLSJ"], ["CAA"], ["CAL"]]
    for i in lista:
        if i[3] == "CTCC":
            listaN[0] += [i]
        elif i[3] == "CTLSC":
            listaN[1] += [i]
        elif i[3] == "CTLSJ":
            listaN[2] += [i]
        elif i[3] == "CAA":
            listaN[3] += [i] 
        elif i[3] == "CAL":
            listaN[4] += [i]   
    return listaN
def crearHTMLSede(lista, sede):
    if sede.upper() == "CTCC":
        file = open("reporteSedeCartago.html", 'w')
        file.write("Centro Tecnologico Central de Cartago")
        for i in lista[0][1:]:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
    elif sede.upper() == "CTLSC":
        file = open("reporteSedeSanCarlos.html", 'w')
        file.write("Centro Tecnologico Local de San Carlos")
        for i in lista[1][1:]:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
    elif sede.upper() == "CTLSJ":
        file = open("reporteSedeSanJose.html", 'w')
        file.write("Centro Tecnologico Local de San Jose")
        for i in lista[2][1:]:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
    elif sede.upper() == "CAA":
        file = open("reporteSedeAlajuela.html", 'w')
        file.write("Centro Academico de Alajuela")
        for i in lista[3][1:]:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
    elif sede.upper() == "CAL":
        file = open("reporteSedeLimon.html", 'w')
        file.write("Centro Academico de Limon")
        for i in lista[4][1:]:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
    else:
        print("Ingrese una sede existente")
    return ""
def HTMLSede(lista):
    crearHTMLSede(lista, "CTCC")
    crearHTMLSede(lista, "CTLSC")
    crearHTMLSede(lista, "CTLSJ")
    crearHTMLSede(lista, "CAA")
    crearHTMLSede(lista, "CAL")
def separarCarrera(lista, carrera):
    listaN = []
    for i in lista:
        if i[4].upper() == carrera.upper():
            listaN += [i]
    return listaN
def crearHTMLCarrera(lista, carrera):
    lista = separarCarrera(lista, carrera)
    file = open("reporte "+carrera+".html", "w")
    if lista != []:
        file.write(carrera)
        for i in lista:
            file.write("\n")
            file.write("\n")
            file.write("Carnet: " + i[0])
            file.write("\n")
            file.write("Nombre: " + i[1])
            file.write("\n")
            file.write("Numero de telefono: " + i[2])
            file.write("\n")
            file.write("Sede: " + i[3])
            file.write("\n")
            file.write("Carrera: " + i[4])
            file.write("\n")
            file.write("Mentor: " + i[5])
            file.write("\n")
            file.write("Correo: " + i[6])
def crearHTMLMentores(lista):
    file = open("reporteMentores.html", "w")
    for i in lista:
        file.write("Sede: " + i[0][2])
        file.write("\n")
        file.write("\n")
        file.write("Nombre del mentor: " + i[0][1])
        file.write("\n")
        file.write("Informacion del ahijado:")
        file.write("\n")
        file.write("Carnet: " + i[1][0]) 
        file.write("\n")
        file.write("Nombre: " + i[1][1]) 
        file.write("\n")
        file.write("Telefono: " + i[1][2])
        file.write("\n")
        file.write("Carrera: " + i[1][4]) 
        file.write("\n")
        file.write("Carnet del Mentor: " + i[1][5]) 
        file.write("\n")
        file.write("Correo: " + i[1][6]) 
        file.write("\n")
        file.write("\n")
def enviarCorreos(correo):
    global archivo
    mensaje = MIMEMultipart ("plain")
    mensaje["From"] = "diegoesteban42069@gmail.com"
    usuario = correo
    mensaje["To"] = usuario
    mensaje["Subject"] = "Prueba"
    adjunto = MIMEBase("application", "octect-stream")
    adjunto.set_payload(open(archivo,"rb").read())
    adjunto.add_header("content-Disposition", "attachment; filename = 'Mensaje.txt'")
    mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("diegoesteban42069@gmail.com", "420696969")
    smtp.sendmail("diegoesteban42069@gmail.com", usuario, mensaje.as_string())
    smtp.quit()
def crearExcel(lista1, lista2):
    global archivo
    hora = datetime.datetime.today()
    hora = str(hora)
    archivo = "BDIntegraTEC" + hora[8:10] + "-" + hora[5:7] + "-" + hora[0:4] + "_" + hora[11:13] + "-" + hora[14:16] + ".csv"
    file = open (archivo, "w")
    file.write("Carnet, Nombre, Telefono, Sede, Carrera, Mentor, Correo  \n")
    for i in lista1:
        file.write(i[0]+" "+' , '+i[1]+" "+' , '+i[2]+" "+' , '+i[3]+" "+' , '+i[4]+" "+' , '+i[5]+" "+' , '+i[6] + '\n')
    for i in lista2:
        file.write(i[0]+" "+' , '+i[1]+" "+' , '" 0 "+" "+' , '+i[2]+" "+' , '+i[3]+" "+' , '+" 0 "+" "+' , '+i[4] + '\n')
    return ""
a = listaEstudiantes(listaCE)
asignarMentores(a, listaMentores(listaCE))
crearExcel(getCorreo(a), getCorreo(listaMentores(listaCE)))
enviarCorreos("vega.diego02@gmail.com")