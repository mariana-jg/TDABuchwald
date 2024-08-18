import os
import random

def generar_archivo_txt(cantidad_filas, rango_Ti, rango_Bi, nombre_archivo):
    ruta_carpeta = "Ejemplos"
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    
    with open(ruta_completa, 'w') as archivo:
        archivo.write("T_i,B_i\n")
        for _ in range(cantidad_filas):
            Ti = random.randint(rango_Ti[0], rango_Ti[1])
            Bi = random.randint(rango_Bi[0], rango_Bi[1])
            archivo.write(f"{Ti},{Bi}\n")

cantidad_filas = int(input("Ingrese la cantidad de filas a generar (sin contar la fila T_i,B_i): "))
rango_Ti = tuple(map(int, input("Ingrese el rango para T_i (separado por coma, ej: 0,100): ").split(',')))
rango_Bi = tuple(map(int, input("Ingrese el rango para B_i (separado por coma, ej: 0,100): ").split(',')))
nombre_archivo = input("Ingrese el nombre del archivo de salida: ") + ".txt"

generar_archivo_txt(cantidad_filas, rango_Ti, rango_Bi, nombre_archivo)
