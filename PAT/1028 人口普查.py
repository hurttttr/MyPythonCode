import sys

n = int(input())
min = ['', '1814/09/06']
max = ['', '2014/09/06']
f = 0
for i in range(n):
    name, time = map(str, sys.stdin.readline().split())
    if time < '1814/09/06' or time > '2014/09/06':
        continue
    f += 1
    if time < max[1]:
        max = [name, time]
    if time > min[1]:
        min = [name, time]
if f == 0:
    print('0')
else:
    print(f, max[0], min[0])
