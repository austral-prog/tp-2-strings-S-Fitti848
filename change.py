def change():
    print("Ingresar gasto:")
    gasto = float(input())

    print("Dinero recibido")
    dinero = int(input())


    vuelto = dinero - gasto

    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(round(vuelto % 1 * 100))

if __name__ == "__main__":
    change()