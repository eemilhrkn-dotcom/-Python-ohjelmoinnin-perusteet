luvut = []
while True:
    syöte = input("anna luku(tyhjä lopettaa):")
    if syöte == "":
        break

    luku = int(syöte)
    luvut.append(luku)

luvut.sort(reverse=True)
print("viisi suurinta lukua:")
for luku in luvut[:5]:
     print(luku)
