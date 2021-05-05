M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
vlaue = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]


def fun(t):
    for i in t[:17]:
        if i.isalpha():
            print(t)
            return False
    sum_num = 0
    for i, j in enumerate(t[:17]):
        sum_num += int(j)*vlaue[i]
    return sum_num


n = int(input())
f = 0
for i in range(n):
    t = input().upper()
    if len(t) != 18:
        print(t)
        continue
    ans = fun(t)
    if ans == False:
        f += 1
        continue
    else:
        if M[ans % 11] != t[17]:
            f += 1
            print(t)
if f == 0:
    print('All passed')
