def names():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nc = (nombre + " " + apellido)

    print(nc.lower())
    print(nc.title())
    print(nc.upper())
    print("\t" + nc.lower())

names()