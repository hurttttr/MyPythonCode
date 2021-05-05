N = int(input())
ans_set = set()
for i in range(1, N+1):
    ans_set.add(i//2+i//3+i//5)
print(len(ans_set))
