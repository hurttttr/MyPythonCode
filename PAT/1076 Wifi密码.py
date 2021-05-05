N = int(input())
lst = ['A', 'B', 'C', 'D']
ans = ''
for i in range(N):
    t = input().split()
    for j in t:
        if j[2] == 'T':
            ans += str(lst.index(j[0])+1)
print(ans)
