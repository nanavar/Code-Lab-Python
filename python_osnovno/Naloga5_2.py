#   Naredi igro križci, krožci

def matrika(matrika):
    for y in range(len(matrika)):
        for x in range(len(matrika[y])):
            print(matrika[y][x], end=" ")
        print()

polje = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

for i in range(9):
    x = int(input("Vnesi število x: ")) -1
    y = int(input("Vnesi število y: ")) -1
    polje[y][x] = "o"
    matrika(polje)
    x = int(input("Vnesi število x: ")) -1
    y = int(input("Vnesi število y: ")) -1
    polje[y][x] = "x"
    matrika(polje)
