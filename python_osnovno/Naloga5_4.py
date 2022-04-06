import getpass

#   Naredi igro vislice

beseda = getpass.getpass("Izberi skrivno besedo: ")

prazno = []
poskusi = len(beseda)*3

for i in beseda:
    prazno.append("_")

for i in range(len(beseda)*3):
    crka = input(f"Vnesi crko [Ostalo je še {poskusi} poskusov]:")
    poskusi -= 1
    for j in range(len(beseda)):
        if crka == beseda[j]:
            prazno[j] = crka
        print("".join(prazno))

        if "_" not in prazno:
            print("Bravo, zmagal si!")
            break