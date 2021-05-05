M = int(input())
N = list(map(int, input().split()))
for n in N:
    for j in range(1, 10):
        t = n**2*j
        ln = len(str(n))
        lt = len(str(t))
        if str(n) == str(t)[lt-ln:lt]:
            print(j, t)
            break
    else:
        print('No')
