a = [int(x) for x in input().split()]
if a[0] != 0:
    for i, j in enumerate(a):
        if j != 0 and i != 0:
            print(i, end='')
            a[i] -= 1
            break
for i, j in enumerate(a):
    if j != 0:
        print(str(i)*j, end='')
print()
