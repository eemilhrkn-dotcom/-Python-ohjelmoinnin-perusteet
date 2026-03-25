def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [5, 1, 5, 12, 4]

tulos = laske_summa(luvut)
print("Listan summa on:", tulos)