def solution_reconstruction(n, prev_index):
    solution = []
    while n > 0:
        solution.append(n)
        n = prev_index[n]
    return solution    


def max_enemies_eliminated(x, f):
    n = len(x)
    dp = [0] * (n + 1)
    prev_index = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            new_enemies = min(x[i - 1], f[i - j])
            if dp[j - 1] + new_enemies > dp[i]:
                dp[i] = dp[j - 1] + new_enemies
                prev_index[i] = j - 1

    solution = solution_reconstruction(n, prev_index)
    
    return dp[n], solution[::-1]


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]

    n = int(lines[0])
    x = [int(line) for line in lines[1:n+1]]
    f = [int(line) for line in lines[n+1:]]
    return x, f


if __name__ == "__main__":
    ruta_archivo = input("Ingresa la ruta absoluta del archivo: ")
    x, f = read_data_from_file(ruta_archivo)
    max_enemies, attack_schedule = max_enemies_eliminated(x, f)
    print("Cantidad máxima de enemigos eliminados:", max_enemies)
    print("Momentos en que se realizan los ataques:", attack_schedule)
