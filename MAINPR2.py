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
import re
#!/usr/bin/env python
# -*- coding: utf-8 -*-
archivo = ""
matrizSede = []
#Se extrae la informacion de la pagina del tec
url = "https://www.tec.ac.cr/carreras"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
cuadros = soup.find_all ("div", class_ = "group") #se divide la info segun el codigo html 
info = ""
for i in cuadros:
    info += i.text
info = info.split("\n")
lista = []
for i in info:
    if i != "":
        lista.append(i) #Se crea una lista con las sedes y las carreras
#E: una lista
#S: una lista
#A partir de una lista, divide la lista segun la sede y elimina las carreras repetidas
def crearListaSJ(lista):
    listaSJ = []
    for i in lista[1:]:
        if i.upper() == "CAMPUS TECNOLÓGICO CENTRAL CARTAGO":
            break
        else:
            if i not in listaSJ:
                listaSJ += [i]
    return listaSJ
#E: una lista
#S: una lista
#A partir de una lista, divide la lista segun la sede y elimina las carreras repetidas
def crearListaC (lista):
    listaC = []
    for i in lista[8:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaC:
                listaC += [i]
    return listaC
#E: una lista
#S: una lista
#A partir de una lista, divide la lista segun la sede y elimina las carreras repetidas
def crearListaSC(lista):
    listaSC = []
    for i in lista[48:]:
        if i.upper() == "CENTRO ACADÉMICO DE LIMÓN":
            break
        else:
            if i not in listaSC:
                listaSC += [i]
    return listaSC
#E: una lista
#S: una lista
#A partir de una lista, divide la lista segun la sede y elimina las carreras repetidas
def crearListaL(lista):
    listaL = []
    for i in lista[61:]:
        if i.upper() == "CENTRO ACADÉMICO DE ALAJUELA":
            break
        else:
            if i not in listaL:
                listaL += [i]
    return listaL
#E: una lista
#S: una lista
#A partir de una lista, divide la lista segun la sede y elimina las carreras repetidas
def crearListaA(lista):
    listaA = []
    for i in lista[68:]:
        if i.upper() == "CAMPUS TECNOLÓGICO LOCAL SAN CARLOS":
            break
        else:
            if i not in listaA:
                listaA += [i]
    return listaA
#E: una lista y un numero
#S: una lista
#Crea una lista con numeros aleatorios con la misma longitud que la ingresada
def crearListaR(n, lista):
    listaR = []
    while len(listaR) != len(lista):
        listaR += [random.randint(0,n)]
    return listaR
#E: una lista
#S: un numero
#Suma todos los numeros de una lista
def sumaLista(lista):
    res = 0
    for i in lista:
        res += i
    return res    
#E: un numero y una lista
#S: una lista
#Crea una lista cuya sumatoria de digitos da n    
def crearListaRes(n, lista):
    res = ""
    while n != res:
        i = crearListaR(n, lista)
        res = sumaLista(i)
    return i
#E: una lista y un numero
#S: un diccionario
#Crea un diccionario con keys iguales a las carreras y values iguales a numeros
def asignarE(lista, num):
    dicc = {}
    listaR = crearListaRes(num, lista)
    n = 0
    for i in lista:
        dicc[i] = listaR[n]
        n += 1
    return dicc
#Crea una matriz basado en los numeros dados
def estudiantesPorSede(a,b,c,d,e):
    matrizDicc = [["CTCC", asignarE(crearListaC(lista)[:10], a)],["CTLSC", asignarE(crearListaSC(lista), b)],["CTLSJ", asignarE(crearListaSJ(lista), c)],["CAA", asignarE(crearListaA(lista), d)],["CAL", asignarE(crearListaL(lista), e)]]
    return matrizDicc
#Valida si un str es un numero
def isNum(string):
    try:
        return type(eval(string)) == int
    except:
        return False
#Valida que los digitos ingresados sean numeros
def validarEstudiantesPorSede(a,b,c,d,e):
    if isNum(a) and isNum(b) and isNum(c) and isNum(d) and isNum(e):
        matrizSede = estudiantesPorSede(int(a), int(b), int(c), int(d), int(e))
        return matrizSede
#Obtiene los keys del diccionario indicado
def crearListaCarreras(lista):
    listaN = [] 
    k = lista[1].keys()
    for x in k:
        listaN += [x]
    return listaN
#Obtiene los values del diccionario
def crearListaEstudiantes(lista):
    listaN = [] 
    k = lista[1].values()
    for x in k:
        listaN += [x]
    return listaN
#E: 2 listas
#S: una lista
#Junta las 2 listas en una sola lista con listas
def crearLista(lista1, lista2):
    listaF = []
    for i in lista1:
        listaF += [[i, lista2[0]]]
        lista2.pop(0)
    return listaF
#Dado una lista crea una lista con la informacion del estudiante
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
#Obtiene los digitos de un diccionario y los convierte en una matriz
def listaCE(dicc):
    lista = [["CTCC", crearLista(crearListaCarreras(dicc[0]), crearListaEstudiantes(dicc[0]))], ["CTLSC", crearLista(crearListaCarreras(dicc[1]), crearListaEstudiantes(dicc[1]))], ["CTLSJ", crearLista(crearListaCarreras(dicc[2]), crearListaEstudiantes(dicc[2]))], ["CAA", crearLista(crearListaCarreras(dicc[3]), crearListaEstudiantes(dicc[3]))], ["CAL", crearLista(crearListaCarreras(dicc[4]), crearListaEstudiantes(dicc[4]))]]
    return lista
#Convierte una lista en diccionario
def makeDicc(lista):
    dicc = {}
    for i in lista:
        dicc[i[0]] = i[1:]
    return dicc
#Basado en una lista crea otra con el 0.05 de su capacidad
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
#Crea una lista juntando a los mentores y los estudiantes
def asignarMentores(lista1, lista2):
    listaConjunto = []
    if lista2 == []:
        return []
    for i in lista1:
        if i[3] == lista2[0][2] and i[4] == lista2[0][3]:
            i[5] = lista2[0][0]
            listaConjunto += [[lista2[0], i]]       
            lista2.pop(0)
        if lista2 == []:
            break
    return listaConjunto
#Retorna una lista con el nombre y el apellido de una persona
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
#A los estudiantes agrega el correo
def getCorreo(lista):
    correos = []
    for i in lista:
        contador = 1
        correo =  getNameLastName(i[1])[0][0][:contador] + getNameLastName(i[1])[1][0] + "@estudiantec.cr"
        correos += [correo]
        i[-1] = correo
    return lista
#E: una lista y un carnet
#S: una lista
def encontrarEstudiante(lista, carnet):
    for i in lista:
        if i[0] == carnet:
            return i
    return []
#Cambia los valores de un estudiante por los ingresados
def actualizarEstudiante(carnet, nombre, telefono, correo, lista):
    if encontrarEstudiante(lista, carnet) != []:
        print(encontrarEstudiante(lista, carnet))
        for i in lista:
            if i[0] == carnet:
                i[1] = nombre
                i[2] = telefono
                i[6] = correo
    return lista
#Dado una lista la separa por sedes
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
#E: una lista y una sede
#S: 
#Crea un html con la sede insertada
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
#Crea 5 htmls con todas las sedes
def HTMLSede(lista):
    crearHTMLSede(lista, "CTCC")
    crearHTMLSede(lista, "CTLSC")
    crearHTMLSede(lista, "CTLSJ")
    crearHTMLSede(lista, "CAA")
    crearHTMLSede(lista, "CAL")
    return ""
#E: una lista, y un str
#S: una lista
#Obtiene una lista de listas con todos los estudiantes de esa carrera
def separarCarrera(lista, carrera):
    listaN = []
    for i in lista:
        if i[4].upper() == carrera.upper():
            listaN += [i]
    return listaN
#crea un html de la carrera indicada
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
    return ""
#Crea un html con el nombre del mentor y la info de sus ahijados
def crearHTMLMentores(lista):
    file = open("reporteMentores.html", "w")
    if lista == []:
        return ""
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
    return ""
#Valida el correo ingresado
def validarCorreo(correo):
    if re.match("[\w\d.-]+\@[\w\d.-]+\.[\w\d.-_]", correo):
        return True
    return False
#Dado un correo envia un archivo
def enviarCorreos(correo):
    global archivo
    if validarCorreo(correo):
        mensaje = MIMEMultipart ("plain")
        mensaje["From"] = "diegoesteban42069@gmail.com"
        usuario = correo
        mensaje["To"] = usuario
        mensaje["Subject"] = "Reporte de Estudiantes IntegraTEC"
        adjunto = MIMEBase("application", "octect-stream")
        adjunto.set_payload(open(archivo,"rb").read())
        adjunto.add_header("content-Disposition", "attachment; filename = 'BDIntegraTEC.csv'")
        mensaje.attach(adjunto)
        smtp = SMTP("smtp.gmail.com")
        smtp.starttls()
        smtp.login("diegoesteban42069@gmail.com", "420696969")
        smtp.sendmail("diegoesteban42069@gmail.com", usuario, mensaje.as_bytes())
        smtp.quit()
        return ""
#Crea un Excel con la informacion de todos los estudiantes y mentores
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
enviarCorreos("vega.diego02gmail.com")