def isprim(a):
    if a == 2:
        return 1
    elif a % 2 == 0 or a == 1:
        return 0
    else:
        for i in range(3, int(a**0.5)+2, 2):
            if a % i == 0:
                return 0
        return 1


N = int(input())
rank = {}
for i in range(N):
    name = input()
    rank[name] = i+1
K = int(input())
for i in range(K):
    t = input()
    if t in rank:
        if rank[t] == -1:
            s = t+': Checked'
        elif rank[t] == 1:
            s = t+': Mystery Award'
        else:
            if isprim(rank[t]) == 1:
                s = t+': Minion'
            else:
                s = t+': Chocolate'
        rank[t] = -1
    else:
        s = t+': Are you kidding?'
    print(s)
