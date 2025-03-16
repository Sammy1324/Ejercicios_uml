from Person import Person

class Windsor(Person):
    def __init__(self, name):
        super().__init__(name, "Windsor")

    def __str__(self):
        return f"{self.name} {self.lastname}"