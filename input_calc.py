def rectangle():
    base = int(input())
    altura = int(input())

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {base * altura}")
    print(f"Perimetro: {2 * (base + altura)}")


if __name__ == "__main__":
    rectangle()