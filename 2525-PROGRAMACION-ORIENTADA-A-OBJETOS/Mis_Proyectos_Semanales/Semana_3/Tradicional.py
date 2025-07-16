#programacion tradicional

# ¿Por qué es Programación Tradicional?

#1.-Porque usamos funciones separadas para pedir datos, procesarlos y mostrar resultados.
#2.-No hay agrupación de datos y funciones en un solo lugar.
#3.-Los datos se manejan de forma suelta, sin objetos o clases.

def pedir_temperaturas():
    # Esta función pide al usuario la temperatura de cada día y las guarda
    lunes = float(input("Temperatura del lunes (°C): "))    # Pide y convierte a número decimal la temperatura del lunes
    martes = float(input("Temperatura del martes (°C): "))  # Pide la temperatura del martes
    miercoles = float(input("Temperatura del miércoles (°C): ")) # Pide la temperatura del miércoles
    jueves = float(input("Temperatura del jueves (°C): "))  # Pide la temperatura del jueves
    viernes = float(input("Temperatura del viernes (°C): "))# Pide la temperatura del viernes
    sabado = float(input("Temperatura del sábado (°C): "))  # Pide la temperatura del sábado
    domingo = float(input("Temperatura del domingo (°C): "))# Pide la temperatura del domingo
    return lunes, martes, miercoles, jueves, viernes, sabado, domingo
    # Devuelve todas las temperaturas para usarlas en otras funciones

def calcular_promedio(lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    # Esta función recibe las temperaturas y calcula el promedio
    suma = lunes + martes + miercoles + jueves + viernes + sabado + domingo
    # Suma todas las temperaturas recibidas
    promedio = suma / 7
    # Divide la suma entre 7 días para obtener el promedio
    return promedio
    # Devuelve el promedio calculado

def mostrar_temperaturas(lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    # Esta función muestra las temperaturas que recibió
    print("\nEstos son los datos de las temperaturas de cada día en grados centígrados:")
    print(f"Lunes: {lunes} °C")       # Muestra temperatura lunes
    print(f"Martes: {martes} °C")     # Muestra temperatura martes
    print(f"Miércoles: {miercoles} °C") # Muestra temperatura miércoles
    print(f"Jueves: {jueves} °C")     # Muestra temperatura jueves
    print(f"Viernes: {viernes} °C")   # Muestra temperatura viernes
    print(f"Sábado: {sabado} °C")     # Muestra temperatura sábado
    print(f"Domingo: {domingo} °C")   # Muestra temperatura domingo

def mostrar_resultado(prom):
    # Esta función muestra el promedio con dos decimales
    print("\n---------------------------------------------")
    print(f"Promedio semanal de temperatura: {prom:.2f} °C")
    # El :.2f hace que se muestre solo con dos decimales
    print("---------------------------------------------")

# Aquí se llama a la función para pedir las temperaturas y se guarda en 'datos'
datos = pedir_temperaturas()
# Se muestran las temperaturas que el usuario ingresó
mostrar_temperaturas(*datos)
# Se calcula el promedio usando los datos ingresados
resultado = calcular_promedio(*datos)
# Se muestra el promedio en pantalla
mostrar_resultado(resultado)