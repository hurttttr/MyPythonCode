str1 = input().upper()
str2 = input().upper()
ans = ''
for i in str1:
    if str2.find(i) == -1 and ans.find(i) == -1:
        if i.isdigit():
            ans += i
        else:
            ans += i.upper()
for i in str2:
    if str1.find(i) == -1 and ans.find(i) == -1:
        if i.isdigit():
            ans += i
        else:
            ans += i.upper()
print(ans)
