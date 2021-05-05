N = int(input())
t = input().split()
sum, num = 0, 0
for i in t:
    try:
        t = float(i)
        if t > 1000 or t < -1000 or (i.find('.') != -1 and len(i)-i.find('.') > 3):
            print('ERROR: %s is not a legal number' % i)
            continue
        sum += t
        num += 1
    except:
        print('ERROR: %s is not a legal number' % i)
if num == 0:
    print('The average of 0 numbers is Undefined')
elif num == 1:
    print('The average of 1 number is %.2f' % sum)
else:
    print('The average of %d numbers is %.2f' % (num, sum/num))
