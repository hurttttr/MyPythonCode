class Student():
    def __init__(self, snumber, sname, csex, a, b, c) -> None:
        self.number = snumber
        self.name = sname
        self.sex = csex
        self.a, self.b, self.c = a, b, c
        self.sumgrade = a+b+c
        self.avegrade = self.sumgrade/3

    def __str__(self) -> str:
        return '{} {} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(
            self.number, self.name, self.sex, self.a, self.b, self.c, self.avegrade, self.sumgrade)


lst = input().split()
a, b, c = map(float, lst[3:])
student = Student(lst[0], lst[1], lst[2], a, b, c)
print(student)
