from turtle import *

#   Nariši zvezdo

x = int(input("Vnesi število kotov: "))
s = int(input("Vnesi dolžino stranice: "))
l = int(input("Vnesi število likov: "))

def narisi_lik(x,s):
    speed(0)
    kot = 180 - (((x - 2) * 180) / x)

    for i in range(x):
        forward(s)
        left(kot)

speed(0)
for i in range(l):
    narisi_lik(x,s)
    left(360/l)