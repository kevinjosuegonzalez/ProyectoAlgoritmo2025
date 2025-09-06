# ============================================
# SISTEMA DE CURSOS Y NOTAS
# ============================================

# -------- FUNCIONES --------

def promedio_general(lista_notas):
    """
    Calcula el promedio de todas las notas registradas.
    Precondición: lista_notas no vacía.
    Postcondición: retorna promedio entre 0 y 100.
    """
    return sum(lista_notas) / len(lista_notas)


def esta_aprobado(nota):
    """
    Determina si una nota es aprobada.
    Precondición: nota ∈ [0..100].
    Postcondición: retorna True si nota >= 60, False en otro caso.
    """
    return nota >= 60


# -------- PROCEDIMIENTOS --------

def registrar_curso(lista_cursos, lista_notas):
    """
    Solicita nombre de curso y nota válida, los guarda en listas.
    """
    curso = ""
    while curso.strip() == "":
        curso = input("Ingrese el nombre del curso: ").strip()

    nota = -1
    while nota < 0 or nota > 100:
        try:
            nota = float(input("Ingrese la nota obtenida (0-100): "))
        except ValueError:
            nota = -1
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100.")

    lista_cursos.append(curso)
    lista_notas.append(nota)
    print("Curso registrado con éxito.")


def mostrar_cursos(lista_cursos, lista_notas):
    """
    Muestra todos los cursos con sus notas.
    """
    if not lista_cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos registrados:")
        for i, (curso, nota) in enumerate(zip(lista_cursos, lista_notas), start=1):
            print(f"{i}. {curso} - Nota: {nota}")


def mostrar_promedio_general(lista_notas):
    """
    Calcula y muestra el promedio general.
    """
    if not lista_notas:
        print("No hay cursos registrados.")
    else:
        prom = promedio_general(lista_notas)
        print(f"Promedio general: {prom:.2f}")


def contar_aprobados(lista_notas):
    """
    Cuenta y muestra cursos aprobados y reprobados.
    """
    if not lista_notas:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for nota in lista_notas if esta_aprobado(nota))
        reprobados = len(lista_notas) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")


# -------- PROGRAMA PRINCIPAL --------

def main():
    lista_cursos = []
    lista_notas = []

    while True:
        print("\n===== MENÚ =====")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_curso(lista_cursos, lista_notas)
        elif opcion == "2":
            mostrar_cursos(lista_cursos, lista_notas)
        elif opcion == "3":
            mostrar_promedio_general(lista_notas)
        elif opcion == "4":
            contar_aprobados(lista_notas)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
