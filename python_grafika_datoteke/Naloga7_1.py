import time
from turtle import *
import random

#   Random beseda iz datoteke na random poziciji

besede = open("besede.txt", "r")
besede = besede.readlines()
filter = []
hideturtle()
screen = Screen()
screen.bgpic("lol.png")
for i in range(len(besede)):
    if len(besede[i]) >= 5:
        filter.append(besede[i])

while True:
    i = random.randint(0, len(filter) -1)
    beseda = filter[i]
    penup()
    goto(random.randint(-500, 500), random.randint(-500, 500))
    pendown()
    clear()
    write(beseda, font=["Arial", 12, "normal"])

    time.sleep(1)
