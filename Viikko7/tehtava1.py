vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("anna kuukauden numero (1-12:)"))

if 1 <= kuukausi <= 12:
    indeksi = (kuukausi %12) //3
    print("vuodenajat on:", vuodenajat[indeksi])
else:
    print("virheellinen kuukauden numero!")

