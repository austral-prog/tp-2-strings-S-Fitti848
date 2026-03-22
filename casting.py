def casting():
    """Lee precio, descuento y cantidad como texto y calcula el
    precio con descuento y el total."""
    pass

    precio=str(input("precio:"))
    descuento= str(input("descuento:"))
    cantidad= str(input("cantidad:"))
    total= (float(precio) - float(descuento))

    print("precio con descuento:",(total))
    print("total:",total * int(cantidad))


casting()