from animal import Animal

class Dog(Animal):


    def __init__(self, name="Anon", colour="Black", limbcount=4, taillength = 25.0):
        super().__init__(name, colour, limbcount)
        self._taillength = taillength

    def get_taillength(self):
        return self._taillength

    def set_taillength(self, taillength):
        if taillength < 0.0:
            taillength = 0.0
        self._taillength = taillength

    taillength = property(get_taillength, set_taillength)

    def bark(self, number):
        s = "woof " * number
        return s