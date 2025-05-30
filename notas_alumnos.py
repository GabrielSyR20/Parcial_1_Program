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


def menu():
    alumnos = []  # Lista para almacenar los alumnos
    notas_alumnos = []  # Lista para almacenar las notas de los alumnos
    notas_cargadas = False  # verificar si las notas han sido cargadas
    
    while True:
        print("\n_____ MENU _____\n"
        "[1] Cargar notas de los alumnos\n" \
        "[2] Mostrar el porcentaje de examenes aprobados por alumno\n" \
        "[3] Mostrar alumno con mejor promedio\n" \
        "[4] Buscar nota\n" \
        "[5] ___ Salir ___")

        opcion = input("Seleccione una opción: ") # Solicitar opción al usuario

        if es_entero(opcion):
            opcion = int(opcion)
            if opcion > 0 and opcion < 6:
                match opcion:
                    case 1:
                        print("Cargando notas de los alumnos...")
                        cant_alumnos, cant_examenes = cargar_alumnos_notas()  # Llamada a la función para cargar alumnos y exámenes
                        alumnos = [cant_alumnos, cant_examenes]
                        notas_alumnos = f.cargar_matriz_notas(alumnos[0], alumnos[1]) # Llamada a la función para cargar las notas de los alumnos
                        print("Notas cargadas al sistema!!")
                        notas_cargadas = True  #verificar que las notas han sido cargadas correctamente
                    case 2:
                        if notas_cargadas:
                            f.porcentaje_aprobados(notas_alumnos) # Llamada a la función para mostrar el porcentaje de exámenes aprobados por alumno
                        else:
                            print("Primero debe cargar las notas de los alumnos!!")
                    case 3:
                        if notas_cargadas:
                            f.mejor_promedio(notas_alumnos) # Llamada a la función para mostrar el alumno con mejor promedio
                        else:
                            print("Primero debe cargar las notas de los alumnos!!")
                    case 4:
                        if notas_cargadas:
                            nota = input("Ingrese la nota que quiere buscar: ")
                            if es_entero(nota):
                                nota = int(nota)
                                posiciones = f.buscar_nota(notas_alumnos, nota)
                                print(posiciones)
                                if posiciones: # Si se encontraron posiciones, mostrar las posiciones donde se encontró la nota

                                    for pos in posiciones:
                                        # pos[0] es el índice del alumno, pos[1] es el índice del examen
                                        print(f"La nota {nota} se encuentra en las siguientes posiciones: "
                                              f"Alumno {pos[0]}, Examen {pos[1]}")
                                        
                                else:
                                    print(f"La nota {nota} no se encontró en ninguna posición.")
                        print("------------------")
                    case 5:
                        for i in range(3):
                            print("Saliendo del programa en", 3 - i, "segundos...")
                        break
            else:
                print("Ingrese una opción válida entre 1 y 5.")
        else:
            print("Ingrese un número entero!!!")


if __name__ == "__main__":
    menu()  # Llamada al menú principal