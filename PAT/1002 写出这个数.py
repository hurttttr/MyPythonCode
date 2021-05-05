n = input()
s = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
n_sum=0
for i in n:
    n_sum+=int(i)
n_sum=str(n_sum)
for index,i in enumerate(n_sum):
    if(index==0):
        print(s[int(i)],end='')
    else:
         print(' %s'%s[int(i)],end='')
print()