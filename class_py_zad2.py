from random import choice

number_trees = int(input("Podaj ilość drzew w lesie: "))


class Tree():
    def __init__(self, srednica=1.0):
        self.srednica = srednica

    def growth(self):
        self.srednica += 0.01

    def gryz(self):
        self.srednica -= 0.07 * self.srednica
        return 0.07 * self.srednica

    def show(self):
        print(f"Średnica drzewa to {self.srednica}m")


class Bobr():
    def __init__(self):
        self.sila = 2.0

    def podgrys(self, tree):
        self.sila -= tree.gryz()
        print(f"Aktualna siła bobra to: {self.sila}")


class Forest():
    def __init__(self):
        self.las = [Tree() for _ in range(number_trees)]
        self.bobr = Bobr()

    def wzrost(self):
        day = 0
        while any(tree.srednica > 0 for tree in self.las):
            print(f"Dzień {day + 1} w lesie")
            day += 1
            x = choice(self.las)
            self.bobr.podgrys(x)
            for tree in self.las:
                tree.growth()
                tree.show()
            print("\n")


las = Forest()
las.wzrost()
