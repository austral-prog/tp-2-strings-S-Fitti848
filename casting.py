def casting():
    precio = input()
    descuento = input()
    cantidad = input()

    p = int(precio)
    d = float(descuento)
    c = int(cantidad)

    precio_con_descuento = p - d

    print(f"Precio: {p}")
    print(f"Descuento: {d}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {precio_con_descuento * c}")


if __name__ == "__main__":
    casting()