A = input()
B = input()
C = A+B
f = [0]*127
for i in C:
    if f[ord(i)] == 0:
        print(i, end='')
        f[ord(i)] = 1
