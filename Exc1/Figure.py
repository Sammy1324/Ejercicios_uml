class Figure:
    def __init__(self, name):
        self.name = name

    def paint(self):
        raise NotImplementedError("Subclass must implement abstract method")