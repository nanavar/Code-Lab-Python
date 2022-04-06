from turtle import *
import time

#   Nariši lik

x = int(input("Vnesi število kotov: "))
s = int(input("Vnesi dolžino stranice: "))

kot = 180 - (((x - 2) * 180) / x)

for i in range(x):
    forward(s)
    speed(1)
    left(kot)