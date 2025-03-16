from Figure import Figure

class Circle(Figure):
    def __init__(self, ratio):
        super().__init__("Circle")
        self.ratio = ratio

    def paint(self):
        print(f"Painting {self.name} with ratio {self.ratio}")