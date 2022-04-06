import random
from getpass import getpass

#   Škarje, papir, kamen

s = 1
p = 2
k = 3

comp_score = 0
user_score = 0

while True:
    comp = random.randint(1,3)
    comp = int(getpass("Drugi igralec vnese število: "))
    if comp == s and user == p:
        comp_score += 1
    elif comp == s and user == k:
        user_score += 1
    elif comp == p and user == k:
        comp_score += 1
    elif user == s and comp == p:
        user_score += 1
    elif user == s and comp == k:
        comp_score += 1
    elif user == p and comp == k:
        user_score += 1
    print(f"Uporabnik ima {user_score} točk, računalnik ima {comp_score} točk.")

    if comp_score == 5 or user_score == 5:
        break




