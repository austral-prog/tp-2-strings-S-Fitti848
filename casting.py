def casting():
    precio = input()
    descuento = input()
    cantidad = input()

    p = int(precio)
    d = float(descuento)
    c = int(cantidad)

    precio_final = p - d

    print(f"Precio: {p}")
    print(f"Descuento: {d}")
    print(f"Precio con descuento: {precio_final}")
    print(f"Total: {precio_final * c}")



casting()