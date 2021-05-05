class Circle():
    PI = 3.14

    def __init__(self, iradius, ix, iy) -> None:
        self.radius = iradius
        self.x = ix
        self.y = iy
        pass

    def calDiameter(self):
        return self.radius*2

    def calArea(self):
        return self.radius**2*self.PI

    def calPerimeter(self):
        return self.calDiameter()*self.PI

    def output(self):
        print('Center=({},{}) and Radius={}'.format(
            self.x, self.y, self.radius))


x, y, r = map(int, input().split())
t = Circle(r, x, y)
print('Diameter={}'.format(t.calDiameter()))
print('Area={:.1f}'.format(t.calArea()))
print('Perimeter={:.1f}'.format(t.calPerimeter()))
