N = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(N-1):
    a = lst.pop(0)
    b = lst.pop(0)
    t = int((a+b)/2)
    for j in range(len(lst)):
        if lst[j] > t:
            lst.insert(j, t)
            break
    else:
        lst.append(t)
print(lst[0])
