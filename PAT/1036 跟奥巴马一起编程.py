lst = [x for x in input().split()]
n = int(lst[0])
print(lst[1]*n)
for i in range(n//2-2+n % 2):
    print(lst[1]+' '*(n-2)+lst[1])
print(lst[1]*n)
