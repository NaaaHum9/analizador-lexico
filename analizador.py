'''
# cargar un archivo.txt
# leer el numero de palabras que contiene
# generar tantos if's como palabras esten en el archivo.txt
# ingresar una palabra y verificar si esta en el archivo mediante los if's
# indicar si esta o no la palabra

    archivo = open("archivo.txt", mode="r")
    print(archivo.readable())# devuelve true si se esta abriendo el archivo y por modo lectura
    print(archivo.read()) # muestra el contenido del archivo
    archivo.close() # cerramos el archivo

#implementacion con terminal


# abrir archivo
def abrirArchivo(nombreArchivo):
    # i = 0
    palabras = []
    with open(nombreArchivo) as archivo: # con with ya se cierra el programa sin tener que declarar el close
        for linea in archivo:
            #print(linea)
            #i = i+1
            palabras.extend(linea.split())
    return palabras
    #conteo = abrirArchivo() #conteo de palabras
    #print(f"Numero de palabras: {conteo}")

# funcion verifica si esta la palabra en la lista 
def verificarPalabra(palabras, buscarPalabra):
    for palabra in palabras:
        if palabra == buscarPalabra:
            return True
    return False

# cargar archivo y contar palabras
nombreArchivo = 'archivo.txt'
palabras = abrirArchivo(nombreArchivo)
print(f"Numero de palabras: {len(palabras)}")

while True:
    # palabra a buscar
    buscarPalabra = input("Ingrese una palabra: ")
    
    #salir del programa
    if buscarPalabra == '0':
        print("Saliendo del programa")
        break

    # vrificar si esta en el archivo
    if verificarPalabra(palabras, buscarPalabra):
        messagebox.showinfo("resultado",f"La palabra {buscarPalabra} esta en el archivo")
    else:
        messagebox.showwarning("resultado",f"La palabra {buscarPalabra} no esta en el archivo")

'''

import tkinter as tk
from tkinter import messagebox

def abrirArchivo(nombreArchivo):
    palabras = []
    with open(nombreArchivo) as archivo: # con with ya se cierra el programa sin tener que declarar el close
        for linea in archivo:
            palabras.extend(linea.split())
    return palabras

def verificarPalabra(palabras, buscarPalabra):
    return buscarPalabra in palabras 

def buscar():
    palabra = entry.get()
    if verificarPalabra(palabras, palabra):
        messagebox.showinfo("Resultado", f"La palabra '{palabra}' esta en el archivo.")
    else:
        messagebox.showinfo("Resultado", f"La palabra '{palabra}' NO esta en el archivo.")

'''------------Interfaz------------'''
# carmagos el archivo
nombreArchivo = 'archivo.txt'
palabras = abrirArchivo(nombreArchivo)

# ventana principal
root = tk.Tk()
root.title("Analizador lexico")
root.geometry("400x300")

# Crear widgets
label = tk.Label(root, text="Ingrese la palabra:", font=("Arial", 14))
label.pack(pady=20)

entry = tk.Entry(root,  font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Probar", command=buscar,  font=("Arial", 14))
button.pack(pady=20)

root.mainloop()