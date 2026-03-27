def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """


    base=int(input("Base:"))
    altura=int(input("Altura:"))
    area=base* altura
    perimetro=2*( base+ altura)
    print(f"Area: {area}")
    print(f"Perimero: {perimetro}")

rectangle()