from decimal import Decimal

n = int(input())
a = list(map(Decimal, input().split(' ')))
result = Decimal(0)
for i in range(n):
    result = result+a[i]*(i+1)*(n-i)
print('%.2f' % result)
