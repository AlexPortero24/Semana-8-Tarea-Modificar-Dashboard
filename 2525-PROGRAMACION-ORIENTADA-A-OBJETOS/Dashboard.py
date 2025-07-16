import os
import subprocess

# Verifica que existan las carpetas necesarias para el funcionamiento del dashboard
# Se añadió la carpeta 'Mis_Proyectos_Semanales' con subcarpetas de Semana_1 a Semana_8
def asegurarse_carpetas_existentes():
    carpetas_necesarias = ['Unidad 1', 'Unidad 2', 'Mis_Proyectos_Semanales']
    for carpeta in carpetas_necesarias:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        # Crea subcarpetas por semana dentro de Mis_Proyectos_Semanales
        if carpeta == 'Mis_Proyectos_Semanales':
            for i in range(1, 9):
                subcarpeta = os.path.join(carpeta, f"Semana_{i}")
                if not os.path.exists(subcarpeta):
                    os.makedirs(subcarpeta)

# Función para mostrar el contenido de un script .py seleccionado
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Función para ejecutar el script seleccionado desde el menú
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

# Muestra el menú principal con las opciones disponibles
def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Se añadió la opción 3 para incluir la carpeta Mis_Proyectos_Semanales
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Mis_Proyectos_Semanales'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Muestra el submenú con las carpetas disponibles dentro de la unidad seleccionada
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Muestra los scripts disponibles en la subcarpeta seleccionada y permite verlos o ejecutarlos
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    asegurarse_carpetas_existentes()
    mostrar_menu()

