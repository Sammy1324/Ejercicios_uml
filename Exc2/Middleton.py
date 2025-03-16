from Person import Person

class Middleton(Person):
    def __init__(self, name):
        super().__init__(name, "Middleton")

    def __str__(self):
        return f"{self.name} {self.lastname}"