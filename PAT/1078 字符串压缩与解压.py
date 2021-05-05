N = input()
ans = []
t = input()
if N == 'C':
    i, num = 0, 1
    while i < len(t):
        if i == len(t)-1:
            if t[i] == t[i-1]:
                ans.append(str(num)+t[i])
            else:
                ans.append(t[i])
        else:
            if t[i] == t[i+1]:
                num += 1
            else:
                if num == 1:
                    ans.append(t[i])
                else:
                    ans.append(str(num)+t[i])
                    num = 1
        i += 1
else:
    num = 0
    f = 0
    for i in t:
        if i.isdigit():
            num = num*10+int(i)
            f = 1
        else:
            if num == 0 and f == 0:
                ans.append(i)
            else:
                for j in range(num):
                    ans.append(i)
            num = 0
            f = 0
print(''.join(ans))
