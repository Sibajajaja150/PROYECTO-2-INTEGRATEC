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
        print('\n',nombreArchivoGrabar,'modificado excitosamente!\n')
        archivo.close()
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
print(listaCE)