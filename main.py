from gestion_contactos import GestionContactos

def main():
    gestion_contactos = GestionContactos()
    gestion_contactos.cargar_contactos()

    while True:
        print("\nMenú:")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestion_contactos.agregar_contacto()
        elif opcion == "2":
            gestion_contactos.mostrar_contactos()
        elif opcion == "3":
            gestion_contactos.buscar_contacto()
        elif opcion == "4":
            gestion_contactos.eliminar_contacto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
