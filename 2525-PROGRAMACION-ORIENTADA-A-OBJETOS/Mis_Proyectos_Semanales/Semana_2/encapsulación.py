# Definición de una clase llamada Persona
class Persona:

    # Método constructor, se llama al crear un objeto de la clase
    def __init__(self, nombre, edad):
        # Atributo privado para el nombre (el doble guion bajo indica que no debe ser accedido directamente desde fuera)
        self.__nombre = nombre
        # Atributo privado para la edad
        self.__edad = edad

        # Método público para mostrar los datos

    def mostrar_datos(self):
        # Accede a los atributos privados y los imprime
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    # Método setter: sirve para cambiar el valor del atributo privado __edad de forma controlada
    def set_edad(self, nueva_edad):
        # Validamos que la edad no sea negativa antes de asignarla
        if nueva_edad >= 0:
            self.__edad = nueva_edad  # Si es válida, se asigna la nueva edad
        else:
            print("La edad no puede ser negativa.")  # Si no es válida, se muestra un mensaje de error

    # Método getter: sirve para obtener el valor del atributo privado __edad
    def get_edad(self):
        return self.__edad  # Devuelve el valor actual de __edad


# Crear un objeto de la clase Persona
persona = Persona("Ana", 25)  # Llama al constructor, asigna nombre y edad

# Mostrar los datos de la persona usando el método público
persona.mostrar_datos()  # Imprime: Nombre: Ana, Edad: 25

# Cambiar la edad de forma segura usando el setter
persona.set_edad(30)  # Cambia la edad a 30 si es válida

# Obtener e imprimir la nueva edad usando el getter
print(f"Nueva edad: {persona.get_edad()}")  # Imprime: Nueva edad: 30

# Intentar asignar una edad inválida
persona.set_edad(-5)  # No permite el cambio y muestra un mensaje: La edad no puede ser negativa.