def trans(n, m):
    f = 0
    s = ''
    if n*m == 0:
        if n == 0:
            s += '0'
        else:
            s += 'Inf'
        return s
    elif n*m < 0:
        f = 1
        n = abs(n)
        m = abs(m)
        s += '(-'
    x = n//m
    if x != 0:
        s += str(x)
        n = n-x*m
    if n % m == 0:
        if f == 1:
            s += ')'
        return s
    if x != 0:
        s += ' '
    t = gcd(n, m)
    s += str('%d/%d' % (n//t, m//t))
    if f == 1:
        s += ')'
    return s


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


a, b, c, d = map(int, input().replace('/', ' ').split())
print('{} + {} = {}'.format(trans(a, b), trans(c, d), trans(a*d+b*c, b*d)))
print('{} - {} = {}'.format(trans(a, b), trans(c, d), trans(a*d-b*c, b*d)))
print('{} * {} = {}'.format(trans(a, b), trans(c, d), trans(a*c, b*d)))
print('{} / {} = {}'.format(trans(a, b), trans(c, d), trans(a*d, b*c)))

'''
import fractions
def format1(num):
    if '/' not in str(num) or abs(num)<1:
        if num<0:
            num = '('+ str(num)+')'
        return num
    else:
        n1, n2 = map(int, str(abs(num)).split('/'))
        if num < 0:
            res = '(-' + str(n1//n2) + ' ' + str(n1%n2)+'/'+str(n2)+')'
        else:
            res = str(n1 // n2) + ' ' + str(n1 % n2) + '/' + str(n2)
        return res

f1, f2 = map(fractions.Fraction, input().split())

print('{} + {} = {}'.format(format1(f1), format1(f2), format1(f1+f2)))
print('{} - {} = {}'.format(format1(f1), format1(f2), format1(f1-f2)))
print('{} * {} = {}'.format(format1(f1), format1(f2), format1(f1*f2)))
if f2==0:
    print('{} / {} = {}'.format(format1(f1), 0, 'Inf'))
else:
    print('{} / {} = {}'.format(format1(f1), format1(f2), format1(f1/f2)))
'''
