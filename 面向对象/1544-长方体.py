class Cuboid():
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def getBottomArea(self):
        return self.length*self.width

    def getVolume(self):
        return self.length*self.width*self.height


cuboid = Cuboid(*map(int, input().split()))
print(cuboid.getBottomArea())
print(cuboid.getVolume())
