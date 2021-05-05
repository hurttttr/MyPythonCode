import sys
l = []
for i in range(3):
    try:
        data = sys.stdin.buffer.readline()
    except:
        while True:
            a = 1
    d = []
    s = bytes()
    for j in range(len(data)-1):
        if data[j:j+1] == b'[':
            s = bytes()
            continue
        if data[j:j+1] == b']':
            d.append(s)
            continue
        s += data[j:j+1]
    l.append(d)

k = int(input())

for i in range(k):
    num = []
    try:
        for j in input().split():
            j = int(j)-1
            if j < 0:
                raise BufferError
            num.append(j)
        if len(num) != 5:
            raise BufferError
        if num[0] >= len(l[0]) or num[4] >= len(l[0]) or num[1] >= len(l[1]) or num[3] >= len(l[1]) or num[2] >= len(l[2]):
            raise BufferError
        result = l[0][num[0]]+b'('+l[1][num[1]]+l[2][num[2]] + \
            l[1][num[3]]+b')'+l[0][num[4]]+b'\n'
    except BufferError:
        result = b'Are you kidding me? @\/@\n'
    sys.stdout.buffer.write(result)
