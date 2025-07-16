# Paso 1: Elige situaciones del mundo real que puedan ser modeladas mediante POO
# ......... Gestión de Mascotas en una Clínica Veterinaria...........

# clinica_veterinaria_v1.py

# Clase que representa al dueño de una mascota

class Dueño:
    def __init__(self, nombre, telefono):
        # Guardamos el nombre y teléfono del dueño
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        # Muestra el nombre y el teléfono del dueño en pantalla
        print(f"Dueño: {self.nombre}, Teléfono: {self.telefono}")


# Clase que representa a una mascota
class Mascota:
    def __init__(self, nombre, especie, edad, dueño):
        # Guardamos los datos básicos de la mascota
        self.nombre = nombre  # nombre de la mascota
        self.especie = especie  # perro, gato, etc.
        self.edad = edad  # edad en años
        self.dueño = dueño  # objeto de la clase Dueño
        self.consultas = []  # lista vacía para guardar sus consultas médicas

    def mostrar_info(self):
        # Muestra información de la mascota y llama al método para mostrar info del dueño
        print(f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}")
        self.dueño.mostrar_info()  # muestra los datos del dueño usando su propio método

    def agregar_consulta(self, motivo, fecha):
        # Crea una nueva consulta con motivo y fecha, y la guarda en la lista
        nueva = Consulta(self, motivo, fecha)
        self.consultas.append(nueva)

    def mostrar_historial(self):
        # Muestra todas las consultas que ha tenido esta mascota
        print(f"Consultas de {self.nombre}:")
        for consulta in self.consultas:
            print(f"- {consulta.motivo} el {consulta.fecha}")


# Clase que representa una consulta veterinaria
class Consulta:
    def __init__(self, mascota, motivo, fecha):
        # Guardamos la mascota a la que pertenece, el motivo y la fecha de la consulta
        self.mascota = mascota
        self.motivo = motivo
        self.fecha = fecha


# Ejemplo de como se usa
# aqui se creo un objeto de la clase Dueño
dueño1 = Dueño("Alex Portero", "0963002378")
# aqui se Creo una mascota asociada a ese dueño
mascota1 = Mascota("Mia", "Gato", 4, dueño1)

# Registramos dos consultas veterinarias para la mascota
mascota1.agregar_consulta("Vacunación", "2025-06-18")
mascota1.agregar_consulta("Desparasitación", "2025-06-22")

print("Mascota:", mascota1.nombre)
print("Dueño:", mascota1.dueño.nombre)

# aqui se muestra toda la información de la mascota y su dueño
mascota1.mostrar_info()
# aqui se muestra todo el historial completo de consultas
mascota1.mostrar_historial()