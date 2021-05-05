n = input()
l = len(n)
s = ['S', 'B']
for index, i in enumerate(n):
    if index != l-1:
        for j in range(int(i)):
            print(s[l-index-2], end='')
    else:
        for i in range(1, int(i)+1):
            print(i, end='')
print()
