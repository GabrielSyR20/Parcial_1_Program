from Validar import *

def cargar_matriz_notas(n, m):
    # devuelve una matriz de las notas de los alumnos
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

def porcentaje_aprobados(matriz):
    aprobados = 0
    total = len(matriz) * len(matriz[0])  # Total de notas

    print(f"Total de notas: {total}")
    for fila in matriz:
        for nota in fila:
            if nota >= 6:  # Consideramos aprobado si la nota es mayor o igual a 6
                aprobados += 1
    return (aprobados / total) * 100 if total > 0 else 0

