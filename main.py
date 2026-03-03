from menu import menu_malteadas

def malteadas():
    while True:
        menu_malteadas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #Se tiene que mostrar las malteadas
            pass
        elif opcion == "2":
            # Tiene que mostrar el historial de las malteadas compradas
            pass
        elif opcion == "3":
            print("Gracias por su preferencia, vuela pronto.")
            break
        else:
            print("Opción no válida, intente con alguna de las opciones propuestas.")


if __name__ == "__main__":
    malteadas()