def fun(s):
    a = [0]*62
    for i in s:
        if i.isdigit():
            a[ord(i)-48] += 1
        elif i.islower():
            a[ord(i)-87] += 1
        else:
            a[ord(i)-29] += 1
    return a


str1 = input()
str2 = input()
a = fun(str1)
b = fun(str2)
count = 0
for i in range(62):
    if b[i] != 0 and b[i] > a[i]:
        count += b[i]-a[i]
if count > 0:
    print('No '+str(count))
else:
    print('Yes '+str(len(str1)-len(str2)))
