n = int(input())
lst = [[eval(x) for x in input().split()]for i in range(n)]
m = int(input())
M = [int(x) for x in input().split()]
for i in M:
    for j in lst:
        if i == j[1]:
            print('%d %d' % (j[0], j[2]))
