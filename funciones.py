from Validar import *

def cargar_matriz_notas(n, m): # devuelve una matriz de las notas de los alumnos
    # n: Número de alumnos
    # m: Número de exámenes
    matriz = []
    for i in range(n):
        fila = []
        print(f"-------- Alumno {i+1} ------")
        for j in range(m):
            while True:
                valor = input(f"Ingrese la nota para el alumno {i+1}: ")
                if es_entero(valor):
                    valor = int(valor)
                    if notas_validas(valor):
                        fila.append(valor)
                        break
                    else:
                        print("Nota no válida, debe ser un número entre 1 y 10")

                else:
                    print("ingresar un valor correcto")
        matriz.append(fila)
    return matriz

def porcentaje_aprobados(matriz): # Calcula el porcentaje de exámenes aprobados por alumno
    # matriz: Matriz de notas de los alumnos
    for i in range(len(matriz)):
        total = 0
        aprobados = 0
        for j in range(len(matriz[i])):
            total += 1
            if matriz[i][j] >= 6:
                aprobados += 1
        porcentaje = (aprobados * 100) / total
        print(f"Alumno {i + 1}: {porcentaje:.2f}% de examenes aprobados")

def mejor_promedio(matriz): # Calcula el alumno con mejor promedio
    # matriz: Matriz de notas de los alumnos
    mejor_prom = 0
    indice = 0

    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        promedio = suma / len(matriz[i])

        if i == 0 or promedio > mejor_prom:
            mejor_prom = promedio
            indice = i

    print(f"El alumno con mejor promedio es el {indice + 1} con un promedio de {mejor_prom:.2f}")
