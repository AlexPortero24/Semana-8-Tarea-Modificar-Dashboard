# El Programa es un conversor de temperaturas.

# El programa tiene como finalidad pasar de grados Celsius a Fahrenheit y Kelvin.

# La idea surgió con el propósito de facilitar la conversión de unidades en la materia de Física 2.
# otra asignatura que también estamos cursando.

# Función que convierte de Celsius a Fahrenheit
# Aquí se utiliza snake_case para el nombre de la función: celsius_a_fahrenheit
def celsius_a_fahrenheit(grados_celsius):  # grados_celsius es tipo float
    return (grados_celsius * 9/5)+32   # El resultado también es un float

# Función que convierte de Celsius a Kelvin
# También usa snake_case para el nombre de la función: celsius_a_kelvin
def celsius_a_kelvin(grados_celsius):  # grados_celsius es float
    return grados_celsius+273.15     # Retorna un float

# Solicita al usuario que ingrese una temperatura en grados Celsius
entrada_temperatura = input("Ingrese los grados Celsius: ")
# entrada_temperatura es un string, ya que input() siempre devuelve texto
# Identificador en snake_case: entrada_temperatura

# Convierte el string ingresado a tipo float para poder hacer cálculos
temperatura_celsius = float(entrada_temperatura)
# Aquí se usa la función float() para convertir un string a float
# Identificador en snake_case: temperatura_celsius

# Llamamos a la función que convierte a Fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
# Se almacena un float como resultado. Identificador en snake_case: temperatura_fahrenheit

# Llamamos a la función que convierte a Kelvin
temperatura_kelvin = celsius_a_kelvin(temperatura_celsius)
# Se almacena un float como resultado. Identificador en snake_case: temperatura_kelvin

# Variable booleana que representa si la conversión fue exitosa
resultado_correcto = True  # Aquí se usa el tipo boolean
# Identificador en snake_case: resultado_correcto

# Aquí se muestra el valor original en Celsius
print("Temperatura en grados Celsius:", temperatura_celsius, "°C")  # float

# Aquí se muestra la temperatura convertida a Fahrenheit
print("Temperatura en grados Fahrenheit:", temperatura_fahrenheit, "°F")  # float

# Aquí se muestra la temperatura convertida a Kelvin
print("Temperatura en grados Kelvin:", temperatura_kelvin, "K")  # float y Kelvin no lleva los grados debido a que es una unidad absoluta.

# Aquí se muestra el estado de la conversión usando una variable booleana
print("¿Conversión realizada correctamente?", resultado_correcto)  # boolean