n = [int(x) for x in input().split()]
f = 0
for i in range(0, len(n)-1, 2):
    if n[i+1] != 0:
        if f != 0:
            print(' ', end='')
        print(n[i]*n[i+1], n[i+1]-1, end='')
        f = 1
if f == 0:
    print('0 0', end='')
print()
