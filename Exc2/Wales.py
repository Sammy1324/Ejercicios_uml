from Windsor import Windsor

class Wales(Windsor):
    def __init__(self, name):
        super().__init__(name)
        self.title = "of Wales"

    def __str__(self):
        return f"{self.name} {self.lastname} {self.title}"