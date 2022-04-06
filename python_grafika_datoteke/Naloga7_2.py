from turtle import *
import time

#   Število pritiskov na sekundo z bazo

hideturtle()

def odstevalnik():
    for i in range(5, 0, -1):
        clear()
        time.sleep(0.1)
        write(i, font=["Arial", 30, "bold",])
        time.sleep(1)
    clear()

def ko_kliknem(x, y):
    clear()
    penup()
    goto(x, y)
    pendown()
    dot(10, "light pink")
    global st_klikov, start
    trenutni = time.time()
    cas = trenutni - start
    if cas < 5:
        st_klikov += 1
        write(f"Klik številka: {st_klikov}", align="center", font=["Arial", 30, "bold"])
    else:
        write(f"Uporabnik je naredil {st_klikov} v 5 sekundah.", align="center", font=["Arial", 30, "bold"])
        time.sleep(5)
        exit()

speed(0)

odstevalnik()

st_klikov = 0
start = time.time()
screen = Screen()
screen.onclick(ko_kliknem)
screen.listen()
screen.mainloop()