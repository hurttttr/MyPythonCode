N = int(input())
max, min = [0, 0], [0, 200]
for i in range(N):
    ID, x, y = map(int, input().split())
    t = (x**2+y**2)**0.5
    if t > max[1]:
        max = [ID, t]
    if t < min[1]:
        min = [ID, t]
print('%04d %04d' % (min[0], max[0]))
