from clovek import Clovek

class App:
    def __int__(self):
        self.visina = 20
        self.sirina = 20
        self.clovek = Clovek()

    def narisi(self):
        for x in range(self.visina):
            for x in range (self.sirina):
                if self.clovek.x == x and self.clovek.y == y:
                    print("Y", end="")
                else:
                    print(".", end="")
                print()