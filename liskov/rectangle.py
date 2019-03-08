
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.height*self.width

    def changeHeight(self, newHeight):
        self.height = newHeight
