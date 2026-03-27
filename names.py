def names():
    nombre = input()
    apellido = input()
    nc = nombre + " " + apellido

    print(nc.lower())
    print(nc.title())
    print(nc.upper())
    print("\t" + nc.lower())

if __name__ == "__main__":
    names()