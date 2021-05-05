'''
str1 = input()
str2 = input()
flag_upper = 0
if str1.find(',') != -1 or str1.find('.') != -1 or str1.find('-') != -1 or str1.find('+') != -1:
    flag_upper = 1
for i in str2:
    if flag_upper == 1:
        if str1.find(i.upper()) == -1 and i.isupper() == False:
            print(i, end='')
    else:
        if str1.find(i.upper()) == -1:
            print(i, end='')
'''
# 测试点4错误  误认为,.-+都代表上档键

str1 = input()
str2 = input()
flag_upper = 0
if str1.find('+') != -1:
    flag_upper = 1
for i in str2:
    if flag_upper == 1:
        if str1.find(i.upper()) == -1 and i.isupper() == False:
            print(i, end='')
    else:
        if str1.find(i.upper()) == -1:
            print(i, end='')
print()
