import time
import random

#   Hitro tipkanje

start = time.time()

st = 0

besedilo = "Note that even though the time is always returned as a floating point number, not all systems provide time with a better precision than 1 second. While this function normally returns non-decreasing values, it can return a lower value than a previous call if the system clock has been set back between the two calls."

besede = besedilo.split()

while True:
    i = random.randint(0, len(besede)-5)
    beseda = " ".join(besede[i: i+5])
    ub_beseda = input(f"Vnesi besedilo [{beseda}]: ")
    if ub_beseda == beseda:
        st += 1
    if st == 3:
        break

end = time.time()
dd = end - start
sek = round(3*5/dd * 60, 2)


print(f"Porabili ste: {sek} besed/sek")