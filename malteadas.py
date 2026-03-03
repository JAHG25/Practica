def pedido_malteadas():
    print("\n Elija la malteada de su preferencia")
    print("1. Malteada de chocolate")
    print("2. Malteada de vainilla")
    print("3. Malteada de fresa")
    print("4. Malteada de galleta")

    opcion = input("Elija una opcion: ")

    malteadas = {
        "1" : "Chocolate",
        "2" : "Vainilla",
        "3" : "Fresa",
        "4" : "Galleta"
    }

    if opcion in malteadas:
        malteada_elegida = malteadas[opcion]
        print("Eligió la malteda de " + malteada_elegida + ", se esta preparando su malteada.")

    else:
        print("Opción no válida, seleccione otra opcion.")

