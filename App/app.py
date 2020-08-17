"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 
import pytest
def loadCSVFile (file1,file2, lst,sep=";"):
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    loadFile(file1, lst,sep, dialect)
    loadFile2 (file2, lst,sep, dialect)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def loadFile (file, lst,sep, dialect):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)        
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    

def loadFile2 (file, lst, sep, dialect):
    
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)        
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
##########
def loadOne(file, lst, sep=";"): 
    del lst[:]
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
    return lst
def loadTwo(file, lst, sep=";"): 
    del lst[:]
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]  
    return lst
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar películas buenas por director")

    
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(director_name,lista1, lista2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    largof1=len(lista1)
    listaone=[]
    for i in range(1,largof1):
            if director_name == lista1[i]["director_name"]:
                id=lista1[i]["id"]
                listaone.append(id)
    
    largof2=len(lista2)
    listavalues=[]
    valores=0
    for j in range (1,largof2):
        valor= float(lista2[j]["vote_average"])
        if lista2[j]["id"] in listaone and valor >= 6:
            valores+=valor
            listavalues.append(valor)
    cuantos=len(listavalues)
    if cuantos==0:
        prom=0
    else:
        prom=round(valores/cuantos,2)
    return [cuantos,prom]

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = [] #instanciar una lista vacia
    lista1=[]
    lista2=[]
    
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/MoviesCastingRaw-small.csv", "Data/SmallMoviesDetailsCleaned.csv", lista) #llamar funcion cargar datos               
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
                
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                criteria =input('Ingrese el criterio de búsqueda\n')
                listaDos=loadTwo( "Data/SmallMoviesDetailsCleaned.csv", lista2)
                counter=countElementsFilteredByColumn(criteria, "original_title" , listaDos) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Escriba el nombre del director: \n')
                listaUno=loadOne("Data/MoviesCastingRaw-small.csv", lista1)
                listaDos=loadTwo( "Data/SmallMoviesDetailsCleaned.csv", lista2)
                counter=countElementsByCriteria(criteria, listaUno,listaDos)
                print("El director", criteria ,"tiene", counter[0], "películas buenas y su promedio es", counter[1] )
           
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()