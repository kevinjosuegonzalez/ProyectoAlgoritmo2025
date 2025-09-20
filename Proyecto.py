
def promedio_general(lista_notas):
    return sum(lista_notas) / len(lista_notas)
def esta_aprobado(nota):
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
    if not lista_cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos registrados:")
        for i, (curso, nota) in enumerate(zip(lista_cursos, lista_notas), start=1):
            print(f"{i}. {curso} - Nota: {nota}")
def mostrar_promedio_general(lista_notas):
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
def registrar_curso(cursos, notas):
    curso = input("Ingrese el nombre del curso: ").strip()
    nota = float(input("Ingrese la nota obtenida (0-100): "))
    cursos.append(curso)
    notas.append(nota)
    print("Curso registrado con éxito.")


def mostrar_cursos(cursos, notas):
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos registrados:")
        for i in range(len(cursos)):
            print(f"{i+1}. {cursos[i]} - Nota: {notas[i]}")


def promedio_general(notas):
    return sum(notas) / len(notas)


def mostrar_promedio_general(notas):
    if not notas:
        print("No hay cursos registrados.")
    else:
        print(f"Promedio general: {promedio_general(notas):.2f}")


def contar_aprobados(notas):
    if not notas:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for n in notas if n >= 60)
        reprobados = len(notas) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")


def buscar_curso(cursos, notas):
    if not cursos:
        print("No hay cursos registrados.")
        return
    nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    encontrado = False
    for i, curso in enumerate(cursos):
        if nombre in curso.lower():  # coincidencia parcial sin importar mayúsculas
            print(f"Curso encontrado: {cursos[i]} - Nota: {notas[i]}")
            encontrado = True
    if not encontrado:
        print("No se encontró el curso.")


def actualizar_nota(cursos, notas):
    if not cursos:
        print("No hay cursos registrados.")
        return
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip().lower()
    for i, curso in enumerate(cursos):
        if nombre in curso.lower():
            nueva_nota = -1
            while nueva_nota < 0 or nueva_nota > 100:
                try:
                    nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                except ValueError:
                    nueva_nota = -1
            notas[i] = nueva_nota
            print("Nota actualizada correctamente.")
            return
    print("No se encontró el curso.")


def eliminar_curso(cursos, notas):
    if not cursos:
        print("No hay cursos registrados.")
        return
    nombre = input("Ingrese el curso a eliminar: ").strip().lower()
    for i, curso in enumerate(cursos):
        if nombre in curso.lower():
            confirmacion = input(f"¿Está seguro que desea eliminar {curso}? (s/n): ").strip().lower()
            if confirmacion == "s":
                cursos.pop(i)
                notas.pop(i)
                print("Curso eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("No se encontró el curso.")


def main():
    cursos = []
    notas = []

    while True:
        print("\n===== MENÚ =====")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Salir")

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
            buscar_curso(cursos, lista_notas)
        elif opcion == "6":
            actualizar_nota(cursos, lista_notas)
        elif opcion == "7":
            eliminar_curso(cursos, )
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
