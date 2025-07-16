# Importamos lo necesario para crear clases abstractas
from abc import ABC, abstractmethod

# Definimos una clase abstracta llamada Animal
class Animal(ABC):
    # Declaramos un método abstracto que las subclases deberán implementar
    @abstractmethod
    def hacer_sonido(self):
        # Este método no tiene implementación aquí
        # Solo actúa como una "regla" que obliga a las subclases a definirlo
        pass

# Creamos una subclase llamada Perro que hereda de Animal
class Perro(Animal):
    # Implementamos el método abstracto
    def hacer_sonido(self):
        # Aquí especificamos qué sonido hace el perro
        print("El perro dice: ¡Guau!")

# Creamos otra subclase llamada Gato que también hereda de Animal
class Gato(Animal):
    # También implementamos el método hacer_sonido, de forma específica para el gato
    def hacer_sonido(self):
        print("El gato dice: ¡Miau!")

# Si intentáramos hacer esto:
# animal = Animal()  ← Esto daría error porque no se puede instanciar una clase abstracta

# Ahora creamos objetos (instancias) de las clases concretas
perro = Perro()  # Creamos un objeto de la clase Perro
gato = Gato()    # Creamos un objeto de la clase Gato

# Llamamos al método hacer_sonido de cada objeto
# Cada uno ejecutará su propia versión del método
perro.hacer_sonido()  # Imprime: El perro dice: ¡Guau!
gato.hacer_sonido()   # Imprime: El gato dice: ¡Miau!