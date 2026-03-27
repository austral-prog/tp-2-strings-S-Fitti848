def ficha():
    nombre_raw = input()
    email_raw = input()
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    nombre = nombre_raw.strip()
    email = email_raw.lower()

    # Iniciales
    espacio = nombre.find(" ")
    iniciales = (nombre[0] + nombre[espacio + 1]).upper()

    # Usuario: apellido.nombre
    nombre_solo = nombre[:espacio].lower()
    apellido_solo = nombre[espacio + 1:].lower()

    suma = n1 + n2 + n3
    promedio = suma / 3

    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print(f"Nombre: {nombre.title()}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {apellido_solo}.{nombre_solo}")
    print(f"Email valido: {'@' in email}")
    print(f"Dominio: {email[email.find('@') + 1:]}")
    print(f"Nombre para archivo: {nombre.title().replace(' ', '_')}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Codigo secreto: {nombre[::-1].upper()}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {suma // 3}")
    print("=" * 24)


if __name__ == "__main__":
    ficha()