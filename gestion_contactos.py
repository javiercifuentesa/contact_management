import re
from contacto import Contacto

class GestionContactos:
    def __init__(self):
        self.contactos = []
        self.archivo = "contactos.txt"

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        correo = input("Ingrese el correo electrónico del contacto: ")

        if not nombre or not telefono or not correo:
            print("Todos los campos son obligatorios.")
            return

        if not self.validar_correo(correo):
            print("Formato de correo electrónico inválido.")
            return

        contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(contacto)
        self.guardar_contactos()
        print("Contacto agregado exitosamente.")
        
    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos disponibles.")
            return

        print("\n********************")
        print("Lista de contactos:\n")
        for contacto in self.contactos:
            print(contacto)
        print("Total de contactos:", len(self.contactos))
        print("*********************")
        
    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:", contacto)
                encontrado = True
                break

        if not encontrado:
            print("Contacto no encontrado.")
    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        encontrado = False

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                self.guardar_contactos()
                print("Contacto eliminado exitosamente.")
                encontrado = True
                break

        if not encontrado:
            print("Contacto no encontrado.")
    def guardar_contactos(self):
        with open(self.archivo, "w") as file:
            for contacto in self.contactos:
                file.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n")
        print("Contactos guardados exitosamente.")
    def cargar_contactos(self):
        try:
            with open(self.archivo, "r") as file:
                for line in file:
                    nombre, telefono, correo = line.strip().split(",")
                    contacto = Contacto(nombre, telefono, correo)
                    self.contactos.append(contacto)
            print("Contactos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de contactos. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar contactos: {e}")
    def validar_correo(self, correo):
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, correo) is not None
# Esta implementación utiliza clases para representar los contactos y el sistema de gestión de contactos. Los métodos de la clase `GestionContactos` permiten agregar, mostrar, buscar y eliminar contactos. La clase `Contacto` representa un contacto individual con atributos para el nombre, número de teléfono y correo electrónico.
# El programa utiliza un archivo de texto para guardar la lista de contactos y carga los datos al iniciar el programa. La validación del formato del correo electrónico se realiza utilizando una expresión regular.
# El manejo de errores se implementa utilizando try-except para capturar y manejar errores relacionados con el archivo y las operaciones de contacto.
# Espero que esta implementación te sea útil. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!
# Fin del código