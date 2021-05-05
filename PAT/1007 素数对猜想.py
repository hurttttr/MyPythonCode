

'''
l = [1 for i in range(n+1)]
for i in range(2, int(n**0.5)+2):
    if l[i] == 1:
        for j in range(i*i, n+1, i):
            l[j] = 0
count = 0
for i in range(5, n+1):
    if l[i] == 1 and l[i-2] == 1:
        count += 1
print(count)
'''


def fun(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+2, 2):
            if n % i == 0:
                return False
        else:
            return True


n = int(input())
count = 0
for i in range(5, n+1):
    if fun(i) == True and fun(i-2) == True:
        count += 1
print(count)
