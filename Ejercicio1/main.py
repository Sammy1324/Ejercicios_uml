from Circle import Circle
from Square import Square
from Elipse import Elipse
from Rectangle import Rectangle

def main():
    figures = [
        Circle(5),
        Square(10),
        Elipse(10, 5),
        Rectangle(10, 5)
    ]

    for figure in figures:
        figure.paint()
    
if __name__ == "__main__":  
    main()