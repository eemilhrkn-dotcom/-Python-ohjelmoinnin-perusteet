import random


koodi1 = ""
for i in range(3): koodi1 += str(random.randint(0, 9))

koodi2 = ""
for i in range(4): koodi2 += str(random.randint(1, 6))

print("Kolme numeroa:", koodi1)
print("Neljä numeroa:", koodi2)
