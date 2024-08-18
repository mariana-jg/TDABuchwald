from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD

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

def solve_tribu_agua(fuerzas, k):
    n = len(fuerzas)
    
    # Crear el problema
    prob = LpProblem("Problema de la Tribu del Agua", LpMinimize)
    
    # Variables de decision
    x = LpVariable.dicts("x", (range(n), range(k)), cat='Binary')
    z = LpVariable.dicts("z", range(k))
    y = LpVariable("y")
    
    # Restricciones
    for i in range(n):
        prob += lpSum(x[i][j] for j in range(k)) == 1
    
    for j in range(k):
        prob += z[j] == lpSum(fuerzas[i][1] * x[i][j] for i in range(n))
    
    for j in range(k):
        for j_prime in range(k):
            if j != j_prime:
                prob += y >= z[j] - z[j_prime]
                prob += y >= z[j_prime] - z[j]
    
    # Funcion objetivo
    prob += y
    
    # Resolver el problema
    prob.solve(PULP_CBC_CMD())
    
    # Obtener los resultados
    grupos = [[] for _ in range(k)]
    for i in range(n):
        for j in range(k):
            if x[i][j].varValue > 0:
                grupos[j].append(fuerzas[i])
    
    return grupos, y.varValue

if __name__ == "__main__":
    ruta_archivo = input("Ingresa la ruta absoluta del archivo: ")
    k, f = leer_archivo(ruta_archivo)
    mejores_grupos, mejor_costo = solve_tribu_agua(f, k)
    for i, grupo in enumerate(mejores_grupos):
        nombres = [nombre for nombre, _ in grupo]
        print(f"Grupo {i + 1}: {', '.join(nombres)}")
    print("Mejor costo:", mejor_costo)