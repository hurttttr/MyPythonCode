lst = input().upper()
a = [0]*26
for i in lst:
    if i.isalpha():
        a[ord(i)-65] += 1
sum = 0
for i, j in enumerate(a):
    sum += (i+1)*j
if sum == 0:
    print('0 0')
else:
    t = bin(sum)
    print(t[2:].count('0'), t[2:].count('1'))
