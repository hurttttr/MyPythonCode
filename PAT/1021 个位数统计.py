n = list(input())
a = set(n)
b = sorted(list(a))
for i in b:
    num = 0
    for j in n:
        if j == i:
            num += 1
    print(i+':'+str(num))
