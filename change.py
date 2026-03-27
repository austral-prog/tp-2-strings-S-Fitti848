def change():
    gasto = float(input("Ingresar gasto:"))
    dinero = int(input("Dinero recibido:"))

    vuelto = dinero - gasto

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(round(vuelto % 1 * 100))

change()