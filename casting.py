def casting():
    precio = input()
    descuento = input()
    cantidad = input()

    total = (float(precio) - float(descuento))

    print("Precio:", precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", total)
    print("Total:", total * int(cantidad))

casting()