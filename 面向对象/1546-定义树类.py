class Tree():
    def __init__(self, iages) -> None:
        self.ages = iages

    def gorw(self, years):
        self.ages += years

    def showAge(self):
        print('Tree ages:%d' % self.ages)


while True:
    ages, years = map(int, input().split())
    if ages == 0 and years == 0:
        break
    tree = Tree(ages)
    tree.gorw(years)
    tree.showAge()
