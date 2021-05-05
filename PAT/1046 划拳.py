n = int(input())
a = b = 0
for i in range(n):
    lst = [int(x) for x in input().split()]
    ans = lst[0]+lst[2]
    if lst[1] == ans and lst[3] != ans:
        b += 1
    if lst[3] == ans and lst[1] != ans:
        a += 1
print(a, b)
