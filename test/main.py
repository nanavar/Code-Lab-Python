# Ustvarim domeno iz podatkovne zbirke, DB

from app import App
import db

# Preberi DB
app = db.preberi()

# Glavna zanka programa
while True:
    # Nariši trenutno stanje aplikacije na zaslon
    app.narisi()

    # Vnos uporabniskih podatkov, spremenimo stanje aplikacije
    dx = int(input("Vnesi dx: "))
    dy = int(input("Vnesi dy: "))

    # Preveri ce uporabnik hoče program končati
    if dx == 0 or dy ==0:
        break

    # Spremenimo stanje aplikacije
    app.clovek.x += dx
    app.clovek.y += dy

# Shranim stanje aplikacije v DB
db.shrani(app)