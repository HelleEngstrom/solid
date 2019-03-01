from Rectangle import Rectangle
from Square import Square

def run():
    rec = Rectangle(2, 4)
    squ = Square(5)

    print("Area of rectangle: " + str(rec.calculateArea()))
    print("Area of square: " + str(squ.calculateArea()))

    rec.changeHeight(5)

    print("Area of rectangle: " + str(rec.calculateArea()))

    #changeHeight is not a relevat function for a square
    squ.changeHeight(3)

    print("Area of square: " + str(squ.calculateArea()))

    #The square is not a square anymore!


if __name__ == "__main__":
    run()
