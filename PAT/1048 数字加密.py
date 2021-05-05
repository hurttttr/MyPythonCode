A, B = map(list, input().split())
A = A[::-1]
B = B[::-1]
if len(A) > len(B):
    for i in range(len(A)-len(B)):
        B.append('0')
else:
    for i in range(len(B)-len(A)):
        A.append('0')
s = ['J', 'Q', 'K']
result = ''
for i in range(len(A)):
    if i % 2 == 0:
        t = (int(A[i])+int(B[i])) % 13
        if t > 9:
            result += str(s[t-10])
        else:
            result += str(t)
    else:
        t = (int(B[i])-int(A[i]))
        if t < 0:
            t += 10
        result += str(t)
result = result[::-1]
print(result)
