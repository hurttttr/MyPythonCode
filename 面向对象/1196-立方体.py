class Cube():
    obj = 0

    def __init__(self, fedge) -> None:
        self.edge = fedge
        self.obj += 1
        self.area = self.calArea()
        self.volume = self.calVolume()

    def calVolume(self):
        return self.edge**3

    def calArea(self):
        return self.edge**2*6

    def display(self):
        print('obj{} Volume:{:.2f}; Area:{:.2f}'.format(
            self.obj, self.volume, self.area))


n = int(input())
for i in range(n):
    t = Cube(float(input()))
    t.display()
