class zwierze():
  def __init__(self, imie, wiek, gatunek):
     self.imie = imie
     self.wiek = wiek
     self.gatunek = gatunek

  def set_imie(self, imie):
    self.imie = imie
  def get_imie(self):
    return self.imie

  def set_wiek(self, wiek):
    self.wiek = wiek
  def get_wiek(self):
    return self.wiek

  def set_gatunek(self, gatunek):
    self.gatunek = gatunek
  def get_gatunek(self):
    return self.gatunek

  def hello(self):
    print(f"Imię zwierzątka to {self.imie}, ma {self.wiek} lat i jest to {self.gatunek}")

class pies(zwierze):
  def __init__(self, imie, wiek, gatunek, rodzaj):
    super().__init__(imie, wiek, gatunek)
    self.rodzaj = rodzaj

  def set_rodzaj(self, rodzaj):
    self.rodzaj = rodzaj
  def get_rodzaj(self):
    return self.rodzaj

  def hello(self):
    print(f"Imię zwierzątka to {self.imie}, ma {self.wiek} lat, jest to {self.gatunek} i jest {self.rodzaj}")

class kot(zwierze):
  def __init__(self, imie, wiek, gatunek, rodzaj):
    super().__init__(imie, wiek, gatunek)
    self.rodzaj = rodzaj

  def set_rodzaj(self, rodzaj):
    self.rodzaj = rodzaj
  def get_rodzaj(self):
    return self.rodzaj

  def hello(self):
    print(f"Imię zwierzątka to {self.imie}, ma {self.wiek} lat, jest to {self.gatunek} i jest {self.rodzaj}")

class domowezoo():
  def __init__(self):
    self.zoo = []

  def dodaj(self, zwierze):
    self.zoo.append(zwierze)

  def wypisz(self):
    for zwierze in self.zoo:
            zwierze.hello()

pies = pies("Mietek", 8, "pies", "domowy")
kot = kot("Bagryś", 1, "kot", "domowy")

moje_zoo = domowezoo()

moje_zoo.dodaj(pies)
moje_zoo.dodaj(kot)

moje_zoo.wypisz()