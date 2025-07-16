#Programacion utilizando POO

#¿Por qué es Programación Orientada a Objetos (POO)?
#1.-Porque se agrupo los datos y las funciones que trabajan con esos datos dentro de un mismo objeto.


# Aquí se usa la clase, que es una plantilla para crear objetos que guardan datos y funciones
class ClimaSemana:
    # Esta función especial se llama cuando creamos un objeto y crea las variables para guardar datos (encapsulamiento)
    def __init__(self):
        self.lunes = 0        # Variable para temperatura lunes dentro del objeto
        self.martes = 0       # Variable para martes dentro del objeto
        self.miercoles = 0    # Variable para miércoles dentro del objeto
        self.jueves = 0       # Variable para jueves dentro del objeto
        self.viernes = 0      # Variable para viernes dentro del objeto
        self.sabado = 0       # Variable para sábado dentro del objeto
        self.domingo = 0      # Variable para domingo dentro del objeto

    # Método para pedir y guardar temperaturas dentro del objeto
    def ingresar_datos(self):
        self.lunes = float(input("Temperatura del lunes (°C): "))
        self.martes = float(input("Temperatura del martes (°C): "))
        self.miercoles = float(input("Temperatura del miércoles (°C): "))
        self.jueves = float(input("Temperatura del jueves (°C): "))
        self.viernes = float(input("Temperatura del viernes (°C): "))
        self.sabado = float(input("Temperatura del sábado (°C): "))
        self.domingo = float(input("Temperatura del domingo (°C): "))

    # Método para mostrar las temperaturas guardadas dentro del objeto
    def mostrar_temperaturas(self):
        print("\nEstos son los datos de las temperaturas de cada día en grados centígrados:")
        print(f"Lunes: {self.lunes} °C")
        print(f"Martes: {self.martes} °C")
        print(f"Miércoles: {self.miercoles} °C")
        print(f"Jueves: {self.jueves} °C")
        print(f"Viernes: {self.viernes} °C")
        print(f"Sábado: {self.sabado} °C")
        print(f"Domingo: {self.domingo} °C")

    # Método que calcula el promedio usando los datos del objeto
    def calcular_promedio(self):
        suma = (self.lunes + self.martes + self.miercoles + self.jueves +
                self.viernes + self.sabado + self.domingo)
        return suma / 7

    # Método que muestra el promedio con dos decimales
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print("\n---------------------------------------------")
        print(f"Promedio semanal de temperatura: {promedio:.2f} °C")
        print("---------------------------------------------")

# Aquí creamos un objeto llamado 'clima' usando la clase ClimaSemana
clima = ClimaSemana()  # Aquí se usa la clase para crear un objeto concreto
clima.ingresar_datos() # Se llama al método para ingresar datos dentro del objeto
clima.mostrar_temperaturas() # Se muestran las temperaturas guardadas en el objeto
clima.mostrar_promedio() # Se calcula y muestra el promedio desde el objeto