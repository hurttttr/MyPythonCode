lst = list(map(int, input().split()))
sum = 0
for i in range(1, len(lst)):
    for j in range(1, len(lst)):
        if i != j:
            sum += lst[i]*10+lst[j]
print(sum)
