class Student():
    def __init__(self, s) -> None:
        self.number = s[0]
        self.name = s[1]
        self.sex = s[2]
        self.year, self.month, self.day = map(int, s[3:6])
        self.a, self.b, self.c = map(float, s[6:9])
        self.sumgrade = self.a + self.b + self.c
        self.avegrade = self.sumgrade/3

    def __str__(self) -> str:
        return '{} {} {} {} {} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(
            self.number, self.name, self.sex, self.year, self.month,
            self.day, self.a, self.b, self.c, self.avegrade, self.sumgrade)


def insert(dic, s):
    if find(dic, s[0]):
        print('Failed')
    else:
        dic[s[0]] = Student(s)
        print(dic[s[0]])


def find(dic, s):
    if s in dic:
        return True
    else:
        return False


def change(dic, s):
    if find(dic, s[0]):
        dic[s[0]] = Student(s)
        print(dic[s[0]])
    else:
        print('Failed')


def delete(dic, s):
    if find(dic, s):
        del dic[s]
        print('Deleted')
    else:
        print('Failed')


def List(lst, dic):
    for i in lst:
        print(dic[i])


dic = {}
while True:
    order = input().split()
    if order[0] == 'Insert':
        print('Insert:')
        insert(dic, order[1:])
        pass
    elif order[0] == 'Find':
        print('Find:')
        if find(dic, order[1]):
            print(dic[order[1]])
        else:
            print('Failed')
        pass
    elif order[0] == 'Change':
        print('Change:')
        change(dic, order[1:])
        pass
    elif order[0] == 'Delete':
        print('Delete:')
        delete(dic, order[1])
        pass
    elif order[0] == 'Sort':
        print('Sort:')
        if order[1] == 'byid':
            lst = sorted(dic, key=lambda x: dic[x].number)
        elif order[1] == 'bybirthday':
            lst = sorted(dic, key=lambda x: (
                dic[x].year, dic[x].month, dic[x].day))
        else:
            lst = sorted(dic, key=lambda x: dic[x].sumgrade)
        List(lst, dic)
        pass
    else:
        print('Good bye!')
        break
