sanat = ["päärynä", "omena", "appelsiini", "traktori", "auto"]
laskuri = 0
for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print("ylis 5 sanaa:", laskuri)

