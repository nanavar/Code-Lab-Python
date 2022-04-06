#   Ugani skrito število

secret = int(input("Vnesi skrito število: "))
attempts = 0

while True:
    guess = int(input("Vnesi število: "))

    if guess == secret:
        print("Uganil si!")
        break