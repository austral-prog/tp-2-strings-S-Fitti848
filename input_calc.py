def rectangle():
    base_in = input()
    altura_in = input()

    base = int(base_in)
    altura = int(altura_in)

    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {base * altura}")
    print(f"Perimetro: {2 * (base + altura)}")


if __name__ == "__main__":
    rectangle()