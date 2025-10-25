
cursos = []
notas = []
historial_cambios = []  # pila

# ---------- FUNCIONES PRINCIPALES ----------
#Permite agregar cursos y notas, validando entradas
def registrar_curso():
    while True:
        nombre = input("Ingrese el nombre del curso: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
        else:
            try:
                nota = float(input("Ingrese la nota obtenida (0-100): "))
                if 0 <= nota <= 100:
                    cursos.append(nombre)
                    notas.append(nota)
                    print("Curso registrado con éxito.")
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Debe ingresar un número válido.")
        continuar = input("¿Desea registrar otro curso? (s/n): ").lower()
        if continuar == "n":
            break
#Muestra todos los cursos registrados
def mostrar_cursos():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            print("Cursos registrados:")
            for i in range(len(cursos)):
                print(f"{i + 1}. {cursos[i]} - Nota: {notas[i]}")
            break
#Calcula el promedio general de las notas.
def calcular_promedio():
    while True:
        if not notas:
            print("No hay cursos registrados.")
        else:
            promedio = sum(notas) / len(notas)
            print(f"Promedio general: {promedio:.2f}")
            break
#Cuenta cursos aprobados y reprobados
def contar_aprobados():
    while True:
        if not notas:
            print("No hay cursos registrados.")
        else:
            aprobados = sum(1 for n in notas if n >= 60)
            reprobados = len(notas) - aprobados
            print(f"Cursos aprobados: {aprobados}")
            print(f"Cursos reprobados: {reprobados}")
            break
#Busca un curso por nombre
def buscar_lineal():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            nombre = input("Ingrese el nombre del curso: ").strip().lower()
            encontrado = False
            for i in range(len(cursos)):
                if nombre in cursos[i].lower():
                    print(f"Curso encontrado: {cursos[i]} - Nota: {notas[i]}")
                    encontrado = True
                    break
            if not encontrado:
                print("Curso no encontrado.")
        if input("¿Desea buscar otro curso? (s/n): ").lower() == "n":
            break

#Permite modificar la nota de un curso existente.
def actualizar_nota():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            nombre = input("Ingrese el nombre del curso a actualizar: ").strip().lower()
            for i in range(len(cursos)):
                if nombre == cursos[i].lower():
                    try:
                        nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                        if 0 <= nueva_nota <= 100:
                            historial_cambios.append(
                                f"Se actualizó: {cursos[i]} - Nota anterior: {notas[i]} → Nueva nota: {nueva_nota}"
                            )
                            notas[i] = nueva_nota
                            print("Nota actualizada correctamente.")
                        else:
                            print("La nota debe estar entre 0 y 100.")
                    except ValueError:
                        print("Debe ingresar un número válido.")
                    break
            else:
                print("Curso no encontrado.")
        if input("¿Desea actualizar otra nota? (s/n): ").lower() == "n":
            break
            
#Elimina un curso y su nota.
def eliminar_curso():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            nombre = input("Ingrese el curso a eliminar: ").strip().lower()
            for i in range(len(cursos)):
                if nombre == cursos[i].lower():
                    confirmar = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()
                    if confirmar == "s":
                        historial_cambios.append(f"Se eliminó: {cursos[i]} - Nota: {notas[i]}")
                        del cursos[i]
                        del notas[i]
                        print("Curso eliminado correctamente.")
                    else:
                        print("Operación cancelada.")
                    break
            else:
                print("Curso no encontrado.")
        if input("¿Desea eliminar otro curso? (s/n): ").lower() == "n":
            break

#Ordena las notas de mayor a menor (burbuja).
def ordenar_por_nota():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            for i in range(len(notas) - 1):
                for j in range(len(notas) - i - 1):
                    if notas[j] < notas[j + 1]:
                        notas[j], notas[j + 1] = notas[j + 1], notas[j]
                        cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
            print("Cursos ordenados por nota:")
            mostrar_cursos()       
            break
#Ordena cursos alfabéticamente (inserción).
def ordenar_por_nombre():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            for i in range(1, len(cursos)):
                key_nombre = cursos[i]
                key_nota = notas[i]
                j = i - 1
                while j >= 0 and cursos[j].lower() > key_nombre.lower():
                    cursos[j + 1] = cursos[j]
                    notas[j + 1] = notas[j]
                    j -= 1
                cursos[j + 1] = key_nombre
                notas[j + 1] = key_nota
            print("Cursos ordenados por nombre:")
            mostrar_cursos()
            break
#buscar_binaria(): Realiza búsqueda binaria de curso (requiere lista ordenada).
def buscar_binaria():
    while True:
        if not cursos:
            print("No hay cursos registrados.")
        else:
            nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower()
            inicio, fin = 0, len(cursos) - 1
            encontrado = False
            while inicio <= fin:
                medio = (inicio + fin) // 2
                if cursos[medio].lower() == nombre:
                    print(f"Curso encontrado: {cursos[medio]} - Nota: {notas[medio]}")
                    encontrado = True
                    break
                elif cursos[medio].lower() < nombre:
                    inicio = medio + 1
                else:
                    fin = medio - 1
            if not encontrado:
                print("Curso no encontrado. Asegúrese de haber ordenado por nombre.")
        if input("¿Desea realizar otra búsqueda? (s/n): ").lower() == "n":
            break

#Simula una cola de solicitudes de revisión.
def simular_cola():
    while True:
        cola = []
        print("Ingrese curso para revisión (escriba 'fin' para terminar):")
        while True:
            curso = input("> ").strip()
            if curso.lower() == "fin":
                break
            cola.append(curso)
        print("\nProcesando solicitudes:")
        for curso in cola:
            print(f"Revisando: {curso}")
        
        break
#Muestra los últimos cambios realizados.
def mostrar_historial():
    while True:
        if not historial_cambios:
            print("No hay cambios registrados.")
        else:
            print("Historial de cambios recientes:")
            for i, cambio in enumerate(reversed(historial_cambios), start=1):
                print(f"{i}. {cambio}")
            break

# ---------- MENÚ PRINCIPAL ----------

while True:
    print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (burbuja)")
    print("9. Ordenar cursos por nombre (inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1": registrar_curso()
    elif opcion == "2": mostrar_cursos()
    elif opcion == "3": calcular_promedio()
    elif opcion == "4": contar_aprobados()
    elif opcion == "5": buscar_lineal()
    elif opcion == "6": actualizar_nota()
    elif opcion == "7": eliminar_curso()
    elif opcion == "8": ordenar_por_nota()
    elif opcion == "9": ordenar_por_nombre()
    elif opcion == "10": buscar_binaria()
    elif opcion == "11": simular_cola()
    elif opcion == "12": mostrar_historial()
    elif opcion == "13":
        print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
