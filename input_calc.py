def rectangle():
    base = int(input("Base:"))
    altura = int(input("Altura:"))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")

rectangle()