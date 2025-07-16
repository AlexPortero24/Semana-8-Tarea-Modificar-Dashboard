# Programa: Gestión de Mascotas en una Clínica Veterinaria usando Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo en Python
# usando la IDE PyCharm
#¿Para qué sirve este programa?
#Este programa simula un sistema básico de gestión de mascotas (perros y gatos) para una clínica veterinaria. Permite al usuario ingresar los datos de su mascota, registrar vacunas, mostrar su información, escuchar su sonido y describirla brevemente.

# Aqui se Define la clase base llamada Mascota
class Mascota:
    def __init__(self, nombre, edad):  # Método constructor que se ejecuta al crear el objeto
        self._nombre = nombre  # Atributo privado que guarda el nombre de la mascota
        self._edad = edad      # Atributo privado que guarda la edad de la mascota
        self._historial_vacunas = []  # Atributo privado que guarda una lista de vacunas

    def mostrar_info(self):  # Método para mostrar los datos de la mascota
        print(f"Nombre: {self._nombre}")  # Imprime el nombre
        print(f"Edad: {self._edad} años")  # Imprime la edad
        if self._historial_vacunas:  # Si hay vacunas registradas
            print(f"Historial de vacunas: {', '.join(self._historial_vacunas)}")  # Muestra las vacunas
        else:  # Si no hay vacunas registradas
            print("Historial de vacunas: Sin vacunas registradas")  # Muestra mensaje vacío

    def agregar_vacuna(self, vacuna):  # Método para añadir una vacuna al historial
        self._historial_vacunas.append(vacuna)  # Agrega la vacuna a la lista

    def hacer_sonido(self):  # Método general que luego será sobrescrito (polimorfismo)
        print("Sonido genérico de mascota.")  # Imprime un sonido base para mascotas

    def describir(self, detalle=None):  # Método con argumento opcional (polimorfismo por argumentos)
        if detalle:  # Si se da una descripción personalizada
            print(f"{self._nombre} es una mascota {detalle}.")  # Imprime descripción personalizada
        else:  # Si no se da descripción
            print(f"{self._nombre} es una mascota registrada en la clínica.")  # Mensaje general


# Aqui  se crea la clase Perro que hereda de Mascota
class Perro(Mascota):
    def hacer_sonido(self):  # Redefinimos el método hacer_sonido (polimorfismo)
        print("¡Guau! ¡Guau!")  # Sonido específico para perro


# Aqui  se crea la clase Gato que también hereda de Mascota
class Gato(Mascota):
    def hacer_sonido(self):  # Redefinimos el método hacer_sonido (polimorfismo)
        print("¡Miau! ¡Miau!")  # Sonido específico para gato


# Aqui se crea la Función para crear una mascota con los datos que ingresa el usuario
def crear_mascota():
    print("Registro de Mascota")  # Muestra mensaje de bienvenida

    especie = input("¿Es un Perro o un Gato? (escribe perro/gato): ").lower()  # Pregunta la especie
    nombre = input("Ingresa el nombre de la mascota: ")  # Pregunta el nombre
    edad = int(input("Ingresa la edad de la mascota: "))  # Pregunta la edad y la convierte a número

    if especie == "perro":  # Si el usuario escribe "perro"
        mascota = Perro(nombre, edad)  # Se crea un objeto de la clase Perro
    elif especie == "gato":  # Si el usuario escribe "gato"
        mascota = Gato(nombre, edad)  # Se crea un objeto de la clase Gato
    else:  # Si escribe otra cosa
        print("Especie no válida. Se creará una mascota genérica.")  # Mensaje de error
        mascota = Mascota(nombre, edad)  # Se crea un objeto genérico

    return mascota  # Devuelve el objeto creado


# Este es el Bloque principal que inicia el programa
if __name__ == "__main__":  # Verifica que estamos ejecutando este archivo directamente

    mascota_usuario = crear_mascota()  # Crea una mascota con los datos del usuario

    while True:  # Aqui hay un Bucle que muestra el menú repetidamente
        print("\n--- Menú/Inicio ---")  # Muestra el título del menú
        print("1. Mostrar información de la mascota")  # Opción 1
        print("2. Agregar vacuna")  # Opción 2
        print("3. Hacer sonido de la mascota ")  # Opción 3
        print("4. Descriopcion de la mascota")  # Opción 4
        print("5. Salir")  # Opción 5

        opcion = input("Selecciona una opción: ")  # Aquí el  usuario puede elige una opción

        if opcion == "1":  # Si elige 1
            mascota_usuario.mostrar_info()  # Se muestra los datos de la mascota
        elif opcion == "2":  # Si elige 2
            vacuna = input("Ingresa el nombre de la vacuna: ")  # Se Pide el nombre de la vacuna
            mascota_usuario.agregar_vacuna(vacuna)  # SE Agrega la vacuna al historial
            print("Vacuna registrada correctamente.")  # Aquí se da el  Mensaje de confirmación
        elif opcion == "3":  # Si elige 3
            mascota_usuario.hacer_sonido()  # Aqui se llama al método hacer_sonido (polimorfismo)
        elif opcion == "4":  # Si elige 4
            usar_detalle = input("¿Deseas agregar una descripción personalizada? (s/n): ").lower()  # Pregunta si quiere detalle
            if usar_detalle == "s":  # Si responde sí
                detalle = input("Escribe una breve descripción (ej. 'tranquila y juguetona'): ")  # Pide descripción
                mascota_usuario.describir(detalle)  # Aqui se llama al método describir con detalle
            else:  # Si no quiere detalle
                mascota_usuario.describir()  # Aqui se llama al método describir sin argumentos
        elif opcion == "5":  # Si elige 5
            print("¡Gracias por usar el sistema de gestión de mascotas!")  #este es el mensaje de salida
            break  # Sale del bucle
        else:  # Si escribe algo no válido
            print("Opción no válida. Intenta de nuevo.")  # Aqui se mostrara un error