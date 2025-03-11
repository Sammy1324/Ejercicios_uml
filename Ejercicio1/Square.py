from Figure import Figure

class Square(Figure):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def paint(self):
        print(f"Painting {self.name} with side {self.side}")