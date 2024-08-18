import time
from itertools import combinations

def leer_archivo(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Ignorar líneas de comentario
    lines = [line for line in lines if not line.startswith('#')]

    k = int(lines[0].strip())  # La cantidad de grupos está en la primera línea después de los comentarios
    habilidades = []

    for line in lines[1:]:
        try:
            nombre, habilidad = line.split(',')
            habilidades.append((nombre.strip(), int(habilidad.strip())))
        except (IndexError, ValueError) as e:
            print(f"Error procesando la línea: {line.strip()} ({e})")

    return k, habilidades

def calcular_nuevo_costo(costo_actual, habilidades, grupo, i, indice):
    return costo_actual + 2 * habilidades[indice] * grupo[i] - habilidades[indice] ** 2

def backtrack(n, k, habilidades, grupo, asignacion, indice, costo_actual, grupos_ordenados, resultado_minimo, asignacion_optima):
    if indice == n:
        #Caso base: Si ya asigné a todos los maestros a un grupo
        if costo_actual < resultado_minimo[0]:
            resultado_minimo[0] = costo_actual
            asignacion_optima[:] = asignacion[:]
            return resultado_minimo, asignacion_optima
    #Itero sobre los grupos y añado un maestro a un grupo y calculo el nuevo costo por esa asignación
    for i in grupos_ordenados:
        grupo[i] += habilidades[indice]
        nuevo_costo = calcular_nuevo_costo(costo_actual, habilidades, grupo, i, indice)
        asignacion[indice] = i
        
        #Poda: Si la nueva suma de los cuadrados de cada grupo es menor que la que ya tenía, añado otro maestro.
        #Si es mayor, descarto la asignación.
        if nuevo_costo < resultado_minimo[0]:
            backtrack(n, k, habilidades, grupo, asignacion, indice + 1, nuevo_costo, grupos_ordenados, resultado_minimo, asignacion_optima)

        grupo[i] -= habilidades[indice]

def backtrack_tribu_agua(maestros, cant_grupos):
    #Ordenamos las habilidades de mayor a menor para optimización del algoritmo
    habilidades = sorted([habilidad for _, habilidad in maestros], reverse=True)
    #Suma de habilidades de cada grupo
    grupo = [0] * cant_grupos
    #La asignación de grupos se realizará en un vector de forma tal que cada posición de los maestros 
    #tenga el número del grupo al que pertenece, de esta forma reconstruimos la solución.
    grupos_a_repartir = sorted(range(cant_grupos), key=lambda i: grupo[i])
    asignacion = [0] * len(maestros)
    resultado_minimo = [float('inf')]
    asignacion_optima = []
    backtrack(len(maestros), cant_grupos, habilidades, grupo, asignacion, 0, 0, grupos_a_repartir, resultado_minimo, asignacion_optima)
    return resultado_minimo[0], asignacion_optima[:]

def imprimir_tuplas_por_grupo(grupos, maestros):
    grupos_dict = {}
    for i, grupo in enumerate(grupos):
        if grupo not in grupos_dict:
            grupos_dict[grupo] = []
        grupos_dict[grupo].append(maestros[i])
    for grupo, tuplas in grupos_dict.items():
        print(f"Grupo {grupo}:")
        for tupla in tuplas:
            print(f"{tupla}")

if __name__ == "__main__":
    ruta_archivo = input("Ingresa la ruta absoluta del archivo: ")
    k, f = leer_archivo(ruta_archivo)
    mejor_costo, mejores_grupos = backtrack_tribu_agua(f, k)
    print("Mejor costo:", mejor_costo)
    maestros_ordenados = sorted(f, key=lambda x: x[1], reverse=True)
    imprimir_tuplas_por_grupo(mejores_grupos, maestros_ordenados)
