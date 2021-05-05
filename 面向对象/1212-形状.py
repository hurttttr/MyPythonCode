import abc

PI = 3.14


class Shape():

    @abc.abstractmethod
    def calarea(self):
        pass

    @abc.abstractmethod
    def calvolume(self):
        pass


class Cylinder(Shape):

    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.area = self.calarea()
        self.volume = self.calvolume()

    def calarea(self):
        return self.r*self.r*PI*2+self.r*2*PI*self.h

    def calvolume(self):
        return self.r*self.r*PI*self.h


class Ball(Shape):

    def __init__(self, r):
        self.r = r
        self.area = self.calarea()
        self.volume = self.calvolume()

    def calarea(self):
        return self.r**2*PI*4

    def calvolume(self):
        return self.r**3*PI*4/3


class Cube(Shape):

    def __init__(self, d):
        self.d = d
        self.area = self.calarea()
        self.volume = self.calvolume()

    def calarea(self):
        return self.d**2*6

    def calvolume(self):
        return self.d**3


class Cuboid(Shape):

    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
        self.area = self.calarea()
        self.volume = self.calvolume()

    def calarea(self):
        return (self.l*self.w+self.l*self.h+self.w*self.h)*2

    def calvolume(self):
        return self.l*self.h*self.h


n = int(input())
for i in range(n):
    lst = [0]*4
    a, b = map(float, input().split())
    lst[0] = Cylinder(a, b)
    a = float(input())
    lst[1] = Ball(a)
    a = float(input())
    lst[2] = Cube(a)
    a, b, c = map(float, input().split())
    lst[3] = Cuboid(a, b, c)
    for i in range(4):
        print('%.2f %.2f' % (lst[i].area, lst[i].volume))
