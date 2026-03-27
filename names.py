def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """


    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nc=(nombre + " " + apellido)

    print(nc.lower())
    print(nc.title())
    print(nc.upper())
    print("\t" + nc.lower())

names()