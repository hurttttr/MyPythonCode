n = int(input())
lst = [int(x) for x in input().split()]
lstsort = sorted(lst)
ans = []
for i in range(n):
    if lst[i] == lstsort[i]:
        for j in range(i):
            if lst[j] > lst[i]:
                break
        else:
            ans.append(str(lst[i]))
print(len(ans))
if len(ans) == 0:
    print()
else:
    print(' '.join(ans))
