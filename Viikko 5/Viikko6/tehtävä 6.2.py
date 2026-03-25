import random
x = int(input("Kuinka monta tahkoa nopassasi on?:"))
def heitä_noppaa():
    return  random.randint(1, x)

while True:
    tulos = heitä_noppaa()
    print("heitto", tulos)

    if tulos == x:
        break