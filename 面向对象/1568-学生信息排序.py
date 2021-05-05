class Student():
    def __init__(self, s) -> None:
        self.number = s[0]
        self.name = s[1]
        self.sex = s[2]
        self.a, self.b, self.c = map(float, s[3:6])
        self.sumgrade = self.a + self.b + self.c
        self.avegrade = self.sumgrade/3

    def __str__(self) -> str:
        return '{} {} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(
            self.number, self.name, self.sex, self.a, self.b, self.c, self.avegrade, self.sumgrade)


def insert(dic, s):
    dic[s[0]] = Student(s)
    print(dic[s[0]])


def List(lst, dic):
    for i in lst:
        print(dic[i])


dic = {}
while True:
    order = input().split()
    if order[0] == 'INSERT':
        insert(dic, order[1:])
        pass
    elif order[0] == 'LIST':
        lst = sorted(dic, key=lambda x: dic[x].number)
        List(lst, dic)
    else:
        print('Good bye!')
        break
