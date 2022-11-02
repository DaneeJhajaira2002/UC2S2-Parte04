# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

login = ""
clave = ""

def login_usuario():
    global login
    global clave
    print("*** LOGIN **** ")
    login = input("\nNombre de usuario: ")
    clave = input("\nIngrese clave: ")
    

def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "rt", encoding = 'utf8')
    contenido = archivo.read()
    return contenido

def menu():
    print("\n1. Listar personas" )
    print("2. Agregar personas")
    print("3. Salir")

login_usuario()

if(login==leer_archivo("login.txt") and clave==leer_archivo("clave.txt")):
    menu()
    opcion = input("\nIngrese su opcion: ")
else:
    login_usuario()
    if(login==leer_archivo("login.txt") and clave==leer_archivo("clave.txt")):
        menu()
    else:
        print("Gracias... Vuelva pronto")
    
        