class Animal:
    #name = "Anon"
    #colour = "Black"
    #limbcount = 4

    def __init__(self, name="Anon", colour="Black", limbcount=4):
        self.name = name
        self.colour = colour
        self._limbcount = limbcount

    def get_limbcount(self):
        return self._limbcount

    def set_limbcount(self, limbcount):
        if limbcount < 0:
            limbcount = 0
        self._limbcount = limbcount

    limbcount = property(get_limbcount, set_limbcount)

    def eat(self, food):
        return f"I'm an {self.colour} animal called {self.name} using some of my {self._limbcount} limbs to eat {food}"

    def move(self, direction):
        return f"I'm an {self.colour} animal called {self.name} using some of my {self._limbcount} limbs to move {direction}"

    def __str__(self):
        return f"name: {self.name}, colour: {self.colour}, limbcount: {self.limbcount}"

    def __add__(self, other):
        self.colour = self.colour + " " + other.colour
        self.limbcount += other.limbcount
        self.name = self.name + " " + other.name
        return self.__str__()