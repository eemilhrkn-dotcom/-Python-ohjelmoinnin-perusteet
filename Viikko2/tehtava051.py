leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3)

kilot = int(grammat // 1000)
jaannos_grammat = grammat - kilot * 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {jaannos_grammat:.2f} grammaa.")
