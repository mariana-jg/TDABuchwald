def verificador_tribu_agua(fuerzas, k, B, particion):
    
    if len(particion) != len(fuerzas): # O(1)
        return False
    
    fuerzas_particiones = [0] * k
    
    for i, fuerza in enumerate(fuerzas): # O(n)
        particiones_index = particion[i]
        fuerzas_particiones[particiones_index] += fuerza
    
    suma_cuadrados = sum(f ** 2 for f in fuerzas_particiones) # O(k)
    
    return suma_cuadrados <= B