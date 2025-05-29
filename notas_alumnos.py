from Validar import es_entero
import funciones as f

def cargar_alumnos_notas():  # Lista para almacenar los alumnos y sus notas
    cantidad_alumnos = input("Ingrese la cantidad de alumnos: ")  # Número de alumnos
    cantidad_examenes = input("Ingrese la cantidad de exámenes: ")  # Número de exámenes

    while True:
        if es_entero(cantidad_alumnos) and es_entero(cantidad_examenes):
            cantidad_alumnos = int(cantidad_alumnos)
            cantidad_examenes = int(cantidad_examenes)
            break
        else:
            print("ingresar un valor correcto!!")
            return cargar_alumnos_notas()
        
    print(f"Cantidad de alumnos: {cantidad_alumnos}, Cantidad de exámenes: {cantidad_examenes}")
    return cantidad_alumnos, cantidad_examenes  # Retorna la cantidad de alumnos y exámenes

cant_alumnos, cant_examenes = cargar_alumnos_notas()  # Llamada a la función para cargar alumnos y exámenes
#cargar_alumnos_notas()
alumnos = [cant_alumnos, cant_examenes]

notas_alumnos = f.cargar_matriz_notas(alumnos[0], alumnos[1])  # Cargar notas de 10 alumnos con 3 notas cada uno
porcentaje_aprobados = f.porcentaje_aprobados(notas_alumnos)  # Calcular porcentaje de aprobados

print("Notas cargadas al sistema!!")
print(f"Porcentaje de aprobados: {porcentaje_aprobados}%")  # Mostrar porcentaje de aprobados