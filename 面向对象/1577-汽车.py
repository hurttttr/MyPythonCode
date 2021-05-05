class Vehicle():
    def __init__(self, sname, scolor) -> None:
        self.name = sname
        self.color = scolor


class Car(Vehicle):
    def __init__(self, sname, scolor, inumber) -> None:
        super().__init__(sname, scolor)
        self.number = inumber

    def __str__(self) -> str:
        return '''Car's name:{}
Car's color:{}
Car's passengerNumber:{}'''.format(self.name, self.color, self.number)


class Truck(Vehicle):
    def __init__(self, sname, scolor, fweigth) -> None:
        super().__init__(sname, scolor)
        self.weight = fweigth

    def __str__(self) -> str:
        return '''Truck's name:{}
Truck's color:{}
Truck's carryingCapacity:{:.1f}'''.format(self.name, self.color, self.weight)


name, color, t = input().split()
car = Car(name, color, int(t))
print(car)
name, color, t = input().split()
truck = Truck(name, color, float(t))
print(truck)
