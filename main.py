from menu import menu_malteadas
from malteadas import pedido_malteadas
from historial import ver_historial

def malteadas():
    while True:
        menu_malteadas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedido_malteadas()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Gracias por su preferencia, vuelva pronto.")
            break
        else:
            print("Opción no válida, intente con alguna de las opciones propuestas.")


if __name__ == "__main__":
    malteadas()