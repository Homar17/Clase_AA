import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog


nombreArchivo = ''
contenido=''
nuevaVentana=''
contenidoNuevoTexto=''

def buscarArchivo():
    global nombreArchivo
    archivo=tk.filedialog.askopenfile()
    nombreArchivo=archivo.name


def crearArchivo():
    global contenido
    #Leer texto del archivo seleccionado
    with open (nombreArchivo, 'r', encoding='utf-8') as file:
        text = file.read()
        contenido=file.read()
    chardic = dict()  #Guarda repetición de letras
    counter = 0 #Caracteres que se repiten

    for char in text: #Por cada letra
        if char in chardic: #Si ya estaba en el dic() significa que se repite
            if chardic[char] == 1: 
                counter += 1 #Se agrega al contador
            chardic[char] += 1 #Continua el conteo
        else:
            chardic[char] = 1 #Si la letra no esta en el diccionario, la agrega


    # Función para obtener el número de repeticiones de un carácter
    def get_repetitions(item):
        return item[1]

    # Ordenar el diccionario por número de repeticiones de mayor a menor
    sorted_chardic = sorted(chardic.items(), key=get_repetitions, reverse=True)

    # Imprimir el resultado
    for char, repetitions in sorted_chardic:
        print(f"character: {char}, repetitions: {repetitions}")

    print("Total repited characters:", counter)

    with open ('new_text.txt','w', encoding='utf-8') as newtext:
        for char, repetitions in sorted_chardic:
            newtext.write(f"character: {char}, repetitions: {repetitions}\n")

    chardic = dict()  #Guarda repetición de letras
    counter = 0 #Caracteres que se repiten

    for char in text: #Por cada letra
        if char in chardic: #Si ya estaba en el dic() significa que se repite
            if chardic[char] == 1: 
                counter += 1 #Se agrega al contador
            chardic[char] += 1 #Continua el conteo
        else:
            chardic[char] = 1 #Si la letra no esta en el diccionario, la agrega


    # Función para obtener el número de repeticiones de un carácter
    def get_repetitions(item):
        return item[1]

    # Ordenar el diccionario por número de repeticiones de mayor a menor
    sorted_chardic = sorted(chardic.items(), key=get_repetitions, reverse=True)

    # Imprimir el resultado
    for char, repetitions in sorted_chardic:
        print(f"character: {char}, repetitions: {repetitions}")

    print("Total repited characters:", counter)
    def crearArchivo():
        with open ('new_text.txt','w', encoding='utf-8') as newtext:
            for char, repetitions in sorted_chardic:
                newtext.write(f"character: {char}, repetitions: {repetitions}\n")
    
    
    with open(nombreArchivo,'r', encoding='utf-8') as file:
            text = file.read()
    print (text)


def mostrarTexto():
    global nuevaVentana
    global contenidoNuevoTexto
    with open ('new_text.txt', 'r', encoding='utf-8') as file:
            contenidoNuevoTexto = file.read()
    nuevaVentana = Toplevel()
    scrollbar = tk.Scrollbar(nuevaVentana)
    scrollbar.pack(side='right', fill='y')
    
    text_widget = tk.Text(nuevaVentana)
    text_widget.insert(tk.END, contenidoNuevoTexto)
    text_widget.pack(fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
app = tk.Tk()
app.geometry('500x200')

tk.Button(
    app,
    text="Buscar archivo",
    command=buscarArchivo
).pack(
    fill=tk.BOTH,
    expand=True,
)
tk.Button(
    app,
    text="Comprimir",
    command= crearArchivo

).pack(
    fill=tk.BOTH,
    expand=True,
)
tk.Button(
    app,
    text= "Mostrar Texto",
    command= mostrarTexto
).pack(
    fill=tk.BOTH,
    expand=True,
)

app.mainloop()
