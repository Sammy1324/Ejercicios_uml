from Person import Person

class Spencer(Person):
    def __init__(self, name):
        super().__init__(name, "Spencer")

    def __str__(self):
        return f"{self.name} {self.lastname}"