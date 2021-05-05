def fun(a, b):
    num = 0
    for i in a:
        if i == b:
            num += 1
    return num


def com_p(n, m):
    ans = m
    if n == 0:
        return 0
    for i in range(n-1):
        ans = ans*10+m
    return ans


l = [x for x in input().split()]
a = fun(l[0], l[1])
b = fun(l[2], l[3])
print(com_p(a, int(l[1]))+com_p(b, int(l[3])))
