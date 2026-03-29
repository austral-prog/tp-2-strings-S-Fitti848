def change():
    print("Ingresar gasto:")
    gasto_raw = input()
    gasto = float(gasto_raw)

    print("Dinero recibido")
    dinero_raw = input()
    dinero = int(dinero_raw)

    vuelto = dinero - gasto

    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(round((vuelto - int(vuelto)) * 100))

if __name__ == "__main__":
    change()