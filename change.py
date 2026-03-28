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
    vuelto_str = f"{vuelto:.2f}"
    partes = vuelto_str.split(".")

    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(partes[0]))
    print("Centavos:")
    print(int(partes[1]))

if __name__ == "__main__":
    change()
