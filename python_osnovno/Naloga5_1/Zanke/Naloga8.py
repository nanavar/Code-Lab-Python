#   Nariši polovični trikotnik

n = int(input("Vnesi število: "))

for x in range(0, n):
    for y in range(0, x + 1):
        print("*", end="")

    print()