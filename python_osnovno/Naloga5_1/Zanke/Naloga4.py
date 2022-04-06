#   Povprečje poljubnih števil

i = 0
povprecje = 0

while True:
    st = float(input("Vnesi število: "))
    if st == 0:
        break;
    povprecje += st
    i += 1

print("Povprečje števil je: ", povprecje/i)