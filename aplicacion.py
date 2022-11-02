# -- coding: utf-8 --
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

def listar_personas():
    print("\n*** LISTANDO PERSONAS *** \n")
    contenido_nombres = open("nombre.txt", "rt", encoding = 'utf8')
    contenido_apellidos = open("apellido.txt", "rt", encoding = 'utf8')
    contenido_dni = open("dni.txt", "rt", encoding = 'utf8')
    
    lista_nombres = contenido_nombres.read().split("\n")
    lista_apellidos = contenido_apellidos.read().split("\n")
    lista_dni = contenido_dni.read().split("\n")
    
    for i in range(len(lista_nombres)):
        print("\n" + lista_nombres[i] + "\t\t" + lista_apellidos[i] + "\t\t" + lista_dni[i])
    
    
def agregar_personas(nombre, apellido, dni):
    print("\n *** AGREGANDO PERSONAS *** \n")
    archivo_nombres = open("nombre.txt", "at")
    archivo_apellidos = open("apellido.txt", "at")
    archivo_dni = open("dni.txt", "at")
    
    archivo_nombres.write("\n"+nombre)
    archivo_apellidos.write("\n"+apellido)
    archivo_dni.write("\n"+dni)
    
    listar_personas()
    
login_usuario()


if(login==leer_archivo("login.txt") and clave==leer_archivo("clave.txt")):
    menu()
    opcion = input("\nIngrese su opcion: ")
    if opcion == "1":
        listar_personas()
    elif opcion == "2":
        nombre = input("\nIngrese nombre: ")
        apellido = input("\nIngrese apellido: ")
        dni = input("\nIngrese DNI: ")
        agregar_personas(nombre, apellido, dni)
    elif opcion == "3":
        print("Graciass... vuelva prontos")
                
else:
    login_usuario()
    if(login==leer_archivo("login.txt") and clave==leer_archivo("clave.txt")):
        menu()
        opcion = input("\nIngrese su opcion: ")
        if opcion == "1":
            listar_personas()
        elif opcion == "2":
            nombre = input("\nIngrese nombre: ")
            apellido = input("\nIngrese apellido: ")
            dni = input("\nIngrese DNI: ")
            agregar_personas(nombre, apellido, dni)
        elif opcion == "3":
            print("Graciass... vuelva prontos")
    else:
        print("Gracias... Vuelva pronto")
        