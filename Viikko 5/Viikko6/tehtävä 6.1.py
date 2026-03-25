import random
def heitä_noppaa():
    return  random.randint(1, 6)

while True:
    tulos = heitä_noppaa()
    print("heitto", tulos)

    if tulos == 6:
        break