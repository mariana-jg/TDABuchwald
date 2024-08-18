import os
import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        mitad_izq = arr[:mitad]
        mitad_der = arr[mitad:]

        merge_sort(mitad_izq)
        merge_sort(mitad_der)

        merge(arr, mitad_izq, mitad_der)

def merge(arr, izq, der):
    i = j = k = 0

    while i < len(izq) and j < len(der):
        if izq[i][1] / izq[i][0] > der[j][1] / der[j][0]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
        k += 1

    while i < len(izq):
        arr[k] = izq[i]
        i += 1
        k += 1

    while j < len(der):
        arr[k] = der[j]
        j += 1
        k += 1

def calcular_orden_optimo(datos_batallas):
    merge_sort(datos_batallas)
    orden_de_batallas = []
    sumatoria_total = 0
    felicidad_actual = 0
    for i in range(len(datos_batallas)):
        tiempo, peso = datos_batallas[i] #O(logN)
        sumatoria_total += (felicidad_actual + tiempo) * (peso)
        felicidad_actual += tiempo
        orden_de_batallas.append((tiempo, peso))

    #O(N) + #O(N*log(N)) = #O(N*log(N))
    return sumatoria_total, orden_de_batallas

def leer_datos_de_archivo(archivo_path): 
    datos_batallas = []
    with open(archivo_path, 'r') as archivo:
        for indice, linea in enumerate(archivo):
            if indice == 0:
                continue       
            Ti, Bi = map(int, linea.strip().split(','))
            batalla = (Ti, Bi)
            datos_batallas.append(batalla) # 0(N) 
    return datos_batallas

def cargar_archivo():
    ruta_archivo = input("Ingresa la ruta absoluta del archivo: ")
    try:
        if os.path.isabs(ruta_archivo):
            datos_batallas = leer_datos_de_archivo(ruta_archivo)
            sumatoria_total, orden_de_batallas = calcular_orden_optimo(datos_batallas)
            print("\nOrden de las batallas:")
            print(orden_de_batallas)
            print("\nSuma Ponderada:")
            print(sumatoria_total)
            print("\n")
        else:
            print("La ruta no es absoluta.")
    except Exception as e:
        print("Error al cargar el archivo:", e)

if __name__ == "__main__":
    cargar_archivo()
