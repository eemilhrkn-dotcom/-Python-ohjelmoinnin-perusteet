lista = []
while True:
    luku = int(input("uusi arvo:"))

    if luku == 0:
        print("heihei!")
        break

    lista.append(luku)

    print("lista nyt",lista)
    print("lista järjestyksessä", sorted (lista))
