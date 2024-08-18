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

def aproximacion_tribu_agua(fuerzas, k):
    # Inicializar k grupos vacios
    grupos = [[] for _ in range(k)]
    
    # Ordenar las fuerzas de mayor a menor
    fuerzas.sort(key=lambda x: x[1], reverse=True)
    
    # Asignar cada fuerza al grupo con menor suma hasta el momento
    for nombre, fuerza in fuerzas:
        grupo_con_menor_suma = min(grupos, key=lambda grupo: sum(f[1] for f in grupo))
        grupo_con_menor_suma.append((nombre, fuerza))
    
    # Calcular el costo de la aproximacion
    costo = sum(sum(fuerza for _, fuerza in grupo)**2 for grupo in grupos)
    
    return grupos, costo

if __name__ == "__main__":
    ruta_archivo = input("Ingresa la ruta absoluta del archivo: ")
    k, f = leer_archivo(ruta_archivo)
    mejores_grupos, mejor_costo = aproximacion_tribu_agua(f, k)
    for i, grupo in enumerate(mejores_grupos, 1):
        nombres = [nombre for nombre, _ in grupo]
        print(f"Grupo {i}: {', '.join(nombres)}")
    print("Mejor costo:", mejor_costo)