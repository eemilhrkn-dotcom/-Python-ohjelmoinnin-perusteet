import random
maara = int(input("kuinka monta heittoa?"))
summa = 0
for i in range(maara):
    heitto = random.randint(1,6)
    print("heitto", heitto)
    summa = heitto + summa

print("silmalukujen summa on", summa)
