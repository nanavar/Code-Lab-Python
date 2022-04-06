#   Najdi najmanjše pozitivno število

min = None

while True:
    st = int(input("Vnesi število: " ))
    if st == 0:
        break
    if not min or st < min:
        min = st

print(f"Najmanjše število je: {min}")