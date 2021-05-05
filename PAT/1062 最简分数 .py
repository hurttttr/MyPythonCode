def fun(n):
    index = n.find('/')
    t = int(n[:index])/int(n[index+1:])
    return t


def gcd(a, b):
    while(b != 0):
        t = a % b
        a = b
        b = t
    return a


a, b, c = input().split()
a = fun(a)
b = fun(b)
c = int(c)
if a > b:
    a, b = b, a
ans = []
for i in range(1, c):
    if a < i/c < b:
        t = gcd(c, i)
        if t == 1:
            ans.append('{}/{}'.format(int(i/t), int(c/t)))
print(' '.join(ans))
