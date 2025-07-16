# Clase base llamada Animal
class Animal:
    # Método hablar que puede ser sobrescrito por clases hijas
    def hablar(self):
        print("Algunos animales emiten sonidos.")  # Mensaje genérico para animales

# Clase hija llamada Perro que hereda de Animal
class Perro(Animal):
    # Sobrescribimos el método hablar
    def hablar(self):
        print("El perro dice: ¡Guau!")  # Comportamiento específico del perro

# Clase hija llamada Vaca que también hereda de Animal
class Vaca(Animal):
    # Sobrescribimos el método hablar
    def hablar(self):
        print("La vaca dice: ¡Muuu!")  # Comportamiento específico de la vaca

# Función polimórfica que recibe cualquier objeto Animal
def hacer_hablar(animal):
    # Llama al método hablar del objeto recibido, sin importar su clase exacta
    animal.hablar()  # Aquí se aplica polimorfismo: el mismo método se comporta distinto según el objeto

# Crear objeto de la clase Perro
mi_perro = Perro()

# Crear objeto de la clase Vaca
mi_vaca = Vaca()

# Usar la función polimórfica con un perro
hacer_hablar(mi_perro)  # Salida: El perro dice: ¡Guau!

# Usar la función polimórfica con una vaca
hacer_hablar(mi_vaca)   # Salida: La vaca dice: ¡Muuu!