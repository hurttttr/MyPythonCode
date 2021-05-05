n = input().upper()
x = [0]*26
for i in n:
    if i.isupper():
        x[ord(i)-65] += 1
k = x.index(max(x))
print('%c %d' % (chr(k+97), max(x)))
