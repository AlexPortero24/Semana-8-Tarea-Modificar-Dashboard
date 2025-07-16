# Definimos la clase base llamada Vehiculo
class Vehiculo:
    # Constructor de la clase Vehiculo con dos atributos: marca y modelo
    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo público que guarda la marca del vehículo
        self.modelo = modelo    # Atributo público que guarda el modelo del vehículo

    # Método que muestra la información del vehículo
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")  # Imprime los valores de marca y modelo

# Definimos la clase Auto que hereda de Vehiculo (Auto es una subclase de Vehiculo)
class Auto(Vehiculo):
    # Constructor de la clase Auto que además recibe el número de puertas
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre Vehiculo para asignar marca y modelo
        self.puertas = puertas           # Atributo adicional de la clase Auto: número de puertas

    # Método que muestra la información del auto
    def mostrar_info(self):
        super().mostrar_info()           # Llama al método mostrar_info de la clase padre para imprimir marca y modelo
        print(f"Puertas: {self.puertas}")  # Luego añade la información específica del auto: número de puertas

# Crear un objeto de la clase Auto, pasando marca, modelo y número de puertas
mi_auto = Auto("Toyota", "Corolla", 4)  # Se crea un Auto con marca "Toyota", modelo "Corolla" y 4 puertas

# Llamamos al método mostrar_info para ver toda la información del objeto
mi_auto.mostrar_info()
# Salida esperada:
# Marca: Toyota
# Modelo: Corolla
# Puertas: 4