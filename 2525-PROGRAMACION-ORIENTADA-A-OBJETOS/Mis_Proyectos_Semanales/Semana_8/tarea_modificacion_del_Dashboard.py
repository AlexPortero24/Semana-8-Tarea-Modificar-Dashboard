# ============================================================================
# NOTA IMPORTANTE: Solo es el codigo modificado puesto en la semana 8
# Este archivo es una versión modificada de "Dashboard.py" con fines de tarea.
# Está ubicado dentro de la carpeta Semana_8. Solo contiene el código base
# adaptado, pero las funcionalidades están diseñadas originalmente para
# ejecutarse desde la raíz del proyecto.
# Por lo tanto: si se ejecuta desde Semana_8, el comportamiento no será el mismo
# que el del Dashboard original, ya que las rutas y carpetas se manejan desde
# donde se ejecuta el script.
# ============================================================================

import os  # Permite interactuar con el sistema de archivos del sistema operativo
import subprocess  # Permite ejecutar comandos externos o abrir otros programas


# Función que verifica y crea carpetas necesarias en la carpeta actual donde se ejecuta el script
def asegurarse_carpetas_existentes():
    carpetas_necesarias = ['Unidad 1', 'Unidad 2', 'Mis_Proyectos_Semanales']  # Lista de carpetas principales a crear

    for carpeta in carpetas_necesarias:  # Recorre cada nombre de carpeta en la lista
        if not os.path.exists(carpeta):  # Si la carpeta no existe en el directorio actual
            os.makedirs(carpeta)  # La crea automáticamente

        if carpeta == 'Mis_Proyectos_Semanales':  # Si la carpeta es la de proyectos semanales
            for i in range(1, 9):  # Recorre los números del 1 al 8 para crear Semana_1 hasta Semana_8
                subcarpeta = os.path.join(carpeta,
                                          f"Semana_{i}")  # Une el nombre de la carpeta con el nombre de cada semana
                if not os.path.exists(subcarpeta):  # Verifica si esa subcarpeta no existe
                    os.makedirs(subcarpeta)  # La crea


# Función para mostrar el contenido de un archivo Python (.py) en consola
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)  # Convierte la ruta relativa a ruta absoluta
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:  # Abre el archivo con codificación utf-8
            codigo = archivo.read()  # Lee el contenido completo del archivo
            print(f"\n--- Código de {ruta_script} ---\n")  # Muestra un título antes del contenido
            print(codigo)  # Imprime el contenido del archivo
            return codigo  # Devuelve el contenido para usarlo en otras funciones si se necesita
    except FileNotFoundError:
        print("El archivo no se encontró.")  # Si el archivo no existe, muestra este mensaje
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")  # Si hay otro error, muestra el mensaje del error
        return None


# Función para ejecutar un script seleccionado desde el menú
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Si el sistema operativo es Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])  # Abre cmd con el script ejecutándose
        else:  # Si es Linux o Mac
            subprocess.Popen(
                ['xterm', '-hold', '-e', 'python3', ruta_script])  # Abre terminal con el script ejecutándose
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")  # Muestra mensaje si no puede ejecutar el script


# Función para mostrar el menú principal del programa
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)  # Define la carpeta actual donde se encuentra el script como base

    unidades = {  # Diccionario que define las opciones del menú principal
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Mis_Proyectos_Semanales'  # Añadido para incluir las semanas de proyectos
    }

    while True:  # Bucle que mantiene activo el menú principal hasta que el usuario elija salir
        print("\nMenu Principal - Dashboard")  # Muestra el título del menú
        for key in unidades:  # Recorre cada clave del diccionario para mostrar las opciones
            print(f"{key} - {unidades[key]}")  # Imprime cada opción del menú con su número
        print("0 - Salir")  # Muestra la opción para salir del menú

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")  # Solicita al usuario que elija una opción
        if eleccion_unidad == '0':
            print("Saliendo del programa.")  # Si elige 0, se cierra el programa
            break
        elif eleccion_unidad in unidades:  # Si la opción ingresada está en el diccionario
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))  # Llama al submenú correspondiente
        else:
            print(
                "Opción no válida. Por favor, intenta de nuevo.")  # Si la opción no es válida, muestra un mensaje de error


# Función para mostrar un submenú con las carpetas dentro de la unidad seleccionada
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if
                    f.is_dir()]  # Lista solo las subcarpetas dentro de la unidad

    while True:  # Bucle para mantener activo el submenú
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):  # Recorre las subcarpetas con un índice numérico
            print(f"{i} - {carpeta}")  # Imprime el número y el nombre de cada subcarpeta
        print("0 - Regresar al menú principal")  # Opción para volver atrás

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")  # Pide al usuario que elija una carpeta
        if eleccion_carpeta == '0':
            break  # Sale del submenú y regresa al menú anterior
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1  # Convierte la entrada del usuario a índice de lista
                if 0 <= eleccion_carpeta < len(sub_carpetas):  # Verifica si la elección es válida
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[
                        eleccion_carpeta]))  # Llama a mostrar_scripts para esa carpeta
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")  # Si la elección no existe, lo avisa
            except ValueError:
                print(
                    "Opción no válida. Por favor, intenta de nuevo.")  # Si el valor ingresado no es un número, muestra error


# Función que muestra los scripts dentro de una subcarpeta y permite al usuario verlos o ejecutarlos
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if
               f.is_file() and f.name.endswith('.py')]  # Lista solo archivos .py

    while True:  # Bucle para el menú de scripts
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):  # Recorre los scripts con su número
            print(f"{i} - {script}")  # Muestra número y nombre de script
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input(
            "Elige un script, '0' para regresar o '9' para ir al menú principal: ")  # Pide al usuario que elija un script
        if eleccion_script == '0':
            break  # Sale al submenú anterior
        elif eleccion_script == '9':
            return  # Regresa al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1  # Convierte la elección en un índice de lista
                if 0 <= eleccion_script < len(scripts):  # Verifica si la elección es válida
                    ruta_script = os.path.join(ruta_sub_carpeta,
                                               scripts[eleccion_script])  # Obtiene la ruta completa del script elegido
                    codigo = mostrar_codigo(ruta_script)  # Muestra el contenido del script
                    if codigo:  # Si el contenido fue leído correctamente
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")  # Pregunta si quiere ejecutarlo
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)  # Ejecuta el script en otra ventana
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")  # Mensaje si no quiere ejecutarlo
                        else:
                            print(
                                "Opción no válida. Regresando al menú de scripts.")  # Si ingresó otra cosa, muestra error
                        input(
                            "\nPresiona Enter para volver al menú de scripts.")  # Pausa antes de mostrar de nuevo el menú
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")  # Si el número no corresponde a un script
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")  # Si se ingresó algo que no es número


# Código principal que se ejecuta solo si el archivo se corre directamente, no si se importa desde otro archivo
if __name__ == "__main__":
    asegurarse_carpetas_existentes()  # Crea las carpetas necesarias si no existen
    mostrar_menu()  # Llama al menú principal para iniciar el programa
