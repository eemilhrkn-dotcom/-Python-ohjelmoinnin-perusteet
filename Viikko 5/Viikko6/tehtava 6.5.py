def poista_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista

luvut = [3, 9, 11, 16, 5, 12, 26]

karsittu = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)