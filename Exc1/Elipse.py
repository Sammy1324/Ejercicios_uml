from Figure import Figure

class Elipse(Figure):
    def __init__(self, major, minor):
        super().__init__("Elipse")
        self.major = major
        self.minor = minor

    def paint(self):
        print(f"Painting {self.name} with major {self.major} and minor {self.minor}")