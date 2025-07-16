# Programa: Gestión de Mascotas en una Clínica Veterinaria con Constructores y Destructores opcionales

# Definición de la clase base Mascota
class Mascota:
    def __init__(self, nombre, edad):
        # Constructor: inicializa el objeto cuando se crea una instancia de Mascota o sus subclases
        self._nombre = nombre              # Atributo privado que almacena el nombre de la mascota
        self._edad = edad                  # Atributo privado que almacena la edad de la mascota
        self._historial_vacunas = []      # Lista privada que guarda el historial de vacunas
        print(f" Mascota registrada: {self._nombre}, {self._edad} años.")  # Mensaje confirmando creación

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es eliminado con 'del' o al finalizar el programa
        print(f" Mascota eliminada del sistema: {self._nombre}")  # Mensaje que indica que el objeto fue destruido

    def mostrar_info(self):
       # metodo para mostar la infomacion de la mascota
        print(f"Nombre: {self._nombre}")  # Imprime el nombre
        print(f"Edad: {self._edad} años")  # Imprime la edad
        if self._historial_vacunas:  # Verifica si la lista de vacunas no está vacía
            print(f"Historial de vacunas: {', '.join(self._historial_vacunas)}")  # Muestra las vacunas separadas por comas
        else:
            print("Historial de vacunas: Sin vacunas registradas")  # Mensaje si no hay vacunas

    def agregar_vacuna(self, vacuna):
        #metodo para agregar una vacuna al historial
        self._historial_vacunas.append(vacuna)  # Añade la vacuna a la lista

    def hacer_sonido(self):
        #metodo para hacer sonido, que es sobrescrito en las subclases (polimorfismo)
        print("Sonido genérico de mascota.")  # Sonido base

    def describir(self, detalle=None):
        # Mtodo que describe a la mascota, acepta descripción opcional
        if detalle:  # Si se proporciona una descripción personalizada
            print(f"{self._nombre} es una mascota {detalle}.")  # Imprime la descripción personalizada
        else:
            print(f"{self._nombre} es una mascota registrada en la clínica.")  # Mensaje por defecto


# Subclase Perro que hereda de Mascota
class Perro(Mascota):
    def hacer_sonido(self):
        # Sobrescribe el metodo hacer_sonido para un perro
        print("¡Guau! ¡Guau!")  # Sonido típico de perro


# Subclase Gato que hereda de Mascota
class Gato(Mascota):
    def hacer_sonido(self):
        # Sobrescribe el metodo hacer_sonido para un gato
        print("¡Miau! ¡Miau!")  # Sonido típico de gato


# Función para crear una mascota según datos del usuario
def crear_mascota():
    print("Registro de Mascota")  # Mensaje de inicio para el registro
    especie = input("¿Es un Perro o un Gato? (escribe perro/gato): ").lower()  # Solicita especie y la convierte a minúsculas
    nombre = input("Ingresa el nombre de la mascota: ")  # Solicita el nombre de la mascota
    edad = int(input("Ingresa la edad de la mascota: "))  # Solicita la edad y la convierte a entero

    if especie == "perro":  # Si la especie es perro
        mascota = Perro(nombre, edad)  # Crea una instancia de Perro
    elif especie == "gato":  # Si la especie es gato
        mascota = Gato(nombre, edad)  # Crea una instancia de Gato
    else:
        print("Especie no válida. Se creará una mascota genérica.")  # Mensaje si no es perro ni gato
        mascota = Mascota(nombre, edad)  # Crea una instancia genérica de Mascota

    return mascota  # Devuelve el objeto creado


# Bloque principal de ejecución
if __name__ == "__main__":
    mascota_usuario = crear_mascota()  # Crea la mascota usando la función de registro

    while True:  # Bucle infinito para mostrar el menú hasta que se decida salir
        print("\n--- Menú ---")  # Título del menú
        print("1. Mostrar información de la mascota")  # Opción 1
        print("2. Agregar vacuna")  # Opción 2
        print("3. Hacer sonido de la mascota")  # Opción 3
        print("4. Descripción de la mascota")  # Opción 4
        print("5. Salir del programa")  # Opción 5
        print("6. Eliminar mascota manualmente")  # Opción 6 para eliminar el objeto

        opcion = input("Selecciona una opción: ")  # Solicita la opción al usuario

        if opcion == "1":
            mascota_usuario.mostrar_info()  # Muestra los datos de la mascota
        elif opcion == "2":
            vacuna = input("Ingresa el nombre de la vacuna: ")  # Solicita nombre de vacuna
            mascota_usuario.agregar_vacuna(vacuna)  # Agrega la vacuna al historial
            print("Vacuna registrada correctamente.")  # Confirma registro
        elif opcion == "3":
            mascota_usuario.hacer_sonido()  # Llamaal metodo para hacer sonido (polimorfismo)
        elif opcion == "4":
            usar_detalle = input("¿Deseas agregar una descripción personalizada? (s/n): ").lower()  # Pregunta si quiere descripción personalizada
            if usar_detalle == "s":
                detalle = input("Escribe una breve descripción: ")  # Solicita la descripción
                mascota_usuario.describir(detalle)  # Muestra descripción personalizada
            else:
                mascota_usuario.describir()  # Muestra descripción por defecto
        elif opcion == "5":
            print("¡Gracias por usar el sistema de gestión de mascotas!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa
        elif opcion == "6":
            confirmacion = input("¿Estás seguro de que deseas eliminar la mascota? (s/n): ").lower()  # Pregunta para confirmar eliminación
            if confirmacion == "s":
                del mascota_usuario  # Elimina el objeto y ejecuta el destructor __del__
                print("Mascota eliminada. Ya no puedes realizar más acciones.")  # Mensaje tras eliminación
                break  # Termina el programa porque ya no hay mascota
            else:
                print("La mascota no fue eliminada.")  # Mensaje si decide no eliminar
        else:
            print("Opción no válida. Intenta de nuevo.")  # Mensaje para opción incorrecta