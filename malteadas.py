ARCHIVO_PEDIDO = "pedidos.txt"

def pedido_malteadas():
    print("\n Elija la malteada de su preferencia")
    print("1. Malteada de chocolate")
    print("2. Malteada de vainilla")
    print("3. Malteada de fresa")
    print("4. Malteada de galleta")

    opcion = input("Elija una opción: ")

    malteadas = {
        "1" : "Chocolate",
        "2" : "Vainilla",
        "3" : "Fresa",
        "4" : "Galleta"
    }

    if opcion in malteadas:
        malteada_elegida = malteadas[opcion]
        print("Ha elegido una malteada de " + malteada_elegida + ", su malteada esta siendo preparada")
        with open(ARCHIVO_PEDIDO, "a", encoding="utf-8") as archivo:
            archivo.write(malteada_elegida + "\n")
    else:
        print("Opción no válida, seleccione otra opción.")

