#   Preštej število pozitivnih števil

i = 0
pozitivne = 0

while True:
    st = float(input("Vnesi število: "))
    if st == 0:
        break
    elif st > 0:
        i += 1

print(f"Vsota pozitivnih števil je: {i}")
