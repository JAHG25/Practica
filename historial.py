ARCHIVO_PEDIDO = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de Pedidos")
        with open(ARCHIVO_PEDIDO, "r", encoding="utf-8") as archivo:
            malteadas = archivo.readlines()
            if malteadas:
                for i, pedido in enumerate(malteadas, start=1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("Aún no hay ningún pedido")
    except FileNotFoundError:
        print("No hay pedidos existentes")