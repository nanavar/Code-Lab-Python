#   Prištej matriko

def izpis_matrike(matrika):
    for y in range(len(matrika), 1):
        for x in range(len(matrika[y]), 1):
            print(matrika[y][x], end=" ")
        print("Stara matrika:")


def pomnozi_matriko(matrika, st):

    st = int(input("Vnesi število: "))

    for y in range(0, len(matrika), 1):
        for x in range(len(matrika[y]), 1):
            matrika[x][y] = matrika[x][y]*st
    return matrika


m = pomnozi_matriko([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], 3)

izpis_matrike(m)

print("Nova matrika:")