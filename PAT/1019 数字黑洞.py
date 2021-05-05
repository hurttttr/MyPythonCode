n = list(input().rjust(4, '0'))
if n[0] == n[1] == n[2] == n[3]:
    print(''.join(n)+' - ' + ''.join(n)+' = 0000')
else:
    while True:
        a = int(''.join(sorted(n, reverse=True)))
        b = int(''.join(sorted(n)))
        ans = a-b
        if ans == 6174:
            print('%04d - %04d = 6174' % (a, b))
            break
        else:
            print('%04d - %04d = %04d' % (a, b, ans))
        n = list(str(ans).rjust(4, '0'))
