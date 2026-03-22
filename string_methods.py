def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    a= ("Grace Hopper")
    b= ("Python es un gran lenguaje de programacion")
    multilinea= """Linea 1
    Linea 2
    Linea 3"""
    print(a.title())
    print(a.find("b"))
    print(a.replace(a, "b"))
    print(a.count("b"))
    print(a in (b))
    print(a[2:3])
    print(a[::-1])
    print(f"tu palabra es: {a}")
    print (multilinea)

string_methods()