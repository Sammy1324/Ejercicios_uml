from Figure import Figure

class Rectangle(Figure):
    def __init__(self, base, height):
        super().__init__("Rectangle")
        self.base = base
        self.height = height

    def paint(self):
        print(f"Painting {self.name} with base {self.base} and height {self.height}")