def change():
    print("Ingresar gasto:")
    gasto_raw = input()
    print(gasto_raw)
    gasto = float(gasto_raw)

    print("Dinero recibido")
    dinero_raw = input()
    print(dinero_raw)
    dinero = int(dinero_raw)

    vuelto = dinero - gasto

    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    centavos = round((vuelto - int(vuelto)) * 100)
    print(centavos)

if __name__ == "__main__":
    change()