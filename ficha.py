def ficha():
    nombre = input("Ingrese su nombre completo: ")
    email = input("Ingrese su email completo: ")
    nota1 = input("nota 1:")
    nota2 = input("nota 2:")
    nota3 = input("nota 3:")

    nombre = nombre.strip()

    pos_espacio = nombre.find(" ")

    iniciales2 = (nombre[0] + nombre[pos_espacio + 1])
    nombre2 = nombre[:pos_espacio]
    apellido = nombre[pos_espacio + 1:]
    usuario = f"{apellido.lower()}.{nombre2.lower()}"

    buscar = "@"
    buscar2 = email.find(buscar)
    secreto = nombre[::-1]

    print("""    =================
    FICHA DEL ALUMNO
    =================""")
    print(f"Nombre: {nombre.title()}")
    print(f"Email: {email.lower()}")
    print(f"caracteres en nombre: {len(nombre)}")
    print(f"Iniciales: {iniciales2.upper()}")
    print(f"usuario: {usuario.strip()}")
    print(f"Email valido: {buscar in email}")
    print(f"Dominio: {email[buscar2 + 1:]}")
    print(f"Nombre para archivo: {nombre.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Nombre secreto: {secreto.upper()}")
    print(f"Nota 1: {int(nota1)}")
    print(f"Nota 2: {int(nota2)}")
    print(f"Nota 3: {int(nota3)}")
    print(f"Suma: {int(nota1) + int(nota2) + int(nota3)}")
    print(f"Promedio: {(int(nota1) + int(nota2) + int(nota3)) / 3}")
    print(f"Promedio entero: {(int(nota1) + int(nota2) + int(nota3)) // 3}")
    print("=" * 24)


ficha()