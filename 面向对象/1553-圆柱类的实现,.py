class Cylinder():
    PI = 3.14

    def __init__(self, iradius, iheight) -> None:
        self.radius = iradius
        self.height = iheight
        self.volume = self.getVolume()

    def getVolume(self):
        return self.radius**2*self.PI*self.height


r, h = map(int, input().split())
t = Cylinder(r, h)
print('%.2f' % t.volume)
