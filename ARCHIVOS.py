#elaborado por Esteban Sibaja y Diego Vega
#fecha de creacion: 18/11/2020 8:34pm
#ultima modificacion: XXXX
#version: 3.8.1
#IMPORTACION DE LIBRERIAS
import pickle
from MAINPR2 import *
#funciones
def grabar(nombreArchivoGrabar,lista):
    '''
    funcion: crea o graba la lista en un archivo 
    e: el nombre del archivo y a lista a guardar
    s: prints
    '''
    try:
        archivo = open(nombreArchivoGrabar,'wb')
        pickle.dump(lista,archivo)
        archivo.close()
        return ""
    except:
        print('error al grabar:',nombreArchivoGrabar)
def leer(nombreArchivoLeer):
    '''
    funcion: leer el archivo 
    e: nombre del archivo a leer
    s: prints 
    '''
    lista = []
    try:
        archivo = open(nombreArchivoLeer,'rb')
        lista = pickle.load(archivo)
        archivo.close()
    except:
        print('error al leer:',nombreArchivoLeer)
    return lista 
#print(listaCE)
def asignarLista(lista,archivo):
    '''
    funcion: lee un archivo y los asigna a variable
    e:lista y archivo
    s:
    '''
    lista = leer(archivo)
    return lista
def setLista(lista,archivo):
    '''
    funcion: agarra datos de una var global y los guarda en lista
    e: lista y archivo
    s: lista 
    '''
    grabar(archivo,lista)
    return []
def existeArch(lista,archivo):
    '''
    busca y verifica que exista un archivo
    e: lista y archivo
    s:
    '''
    try:
        lista = asignarLista(lista,archivo)
        return lista
    except:
        setLista(lista,archivo)
        return lista
def htmlCrear(archivo,mensaje):
    arch = open(archivo,'w')
    arch.write(mensaje)
    arch.close()