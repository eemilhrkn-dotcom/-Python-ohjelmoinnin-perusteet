def gallonat_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    syote = float(input("Paljonko gallonoita?: "))

    if syote < 0:
        break

    litrat = gallonat_litroiksi(syote)
    print(f"Se on noin {litrat:.2f} litraa\n")

print("Valmis!")
