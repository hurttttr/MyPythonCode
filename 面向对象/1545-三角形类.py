class GeometricObject():
    def __init__(self, scolor, sfilled):
        self.color = scolor
        self.filled = sfilled


class Triangle(GeometricObject):
    def __init__(self, scolor, bfilled, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(scolor, bfilled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        p = (self.side1+self.side2+self.side3)/2
        s = (p*(p-self.side1)*(p-self.side2)*(p-self.side3))**0.5
        return s

    def getPerimeter(self):
        return self.side1+self.side2+self.side3

    def __str__(self) -> str:
        return 'Triangle: side1=%.1f side2=%.1f side3=%.1f color=%s filled=%s' % (self.side1, self.side2, self.side3, self.color, self.filled)


a, b, c, color, filled = input().split()
a, b, c = float(a), float(b), float(c)
triangle = Triangle(color, filled, a, b, c)
print(triangle)
print('Area=%.2f' % triangle.getArea())
print('Perimeter=%.2f' % triangle.getPerimeter())
