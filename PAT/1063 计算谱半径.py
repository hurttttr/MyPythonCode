n = int(input())
max = 0
for i in range(n):
    a, b = map(int, input().split())
    t = (a**2+b**2)**0.5
    if t > max:
        max = t
print("{:.2f}".format(max))
