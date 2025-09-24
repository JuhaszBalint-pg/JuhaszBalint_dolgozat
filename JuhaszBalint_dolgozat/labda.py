"""
A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!
"""

print ("csak egész számokat használj!")
d = int( input ("Add meg a labda átmérőjét cm-ben! " ))
mennyiseg = int( input ("Add meg mennyi labdát kell becsomagolni! "))
szalag = int( input ("Add meg a rendelkezére álló szalag hoszzát cm-ben! "))
masni = 60
Pi = float(3.14)
csomagolas = (d*Pi*mennyiseg)*2+masni

#print (f"{csomagolas:.3f} hosszúságú szalag kell a csomagoláshoz")

if csomagolas<=szalag:
    print ("Elégséges szalagod van a csomagolás elvégzéséhez")
else:
    print (f"Nem elégséges! Valahonna szalagot kell még szerezned!")