print("=== Euro zu Türkische Lira Rechner ===")

wechselkurs = 43.50

euro = float(input("Wie viel Euro möchtest du umrechnen? "))

tl = euro * wechselkurs

print("----------------------------")
print("Euro:", euro)
print("Wechselkurs:", wechselkurs)
print("Türkische Lira:", round(tl, 2), "TL")