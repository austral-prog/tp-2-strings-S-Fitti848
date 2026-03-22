def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto:"))
    print(gasto)
    dinero = int(input("Dinero recibido:"))
    print(dinero)

    vuelto = dinero - gasto

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(round(vuelto % 1 * 100))


change()