n = int(input())
now_list = [0 for i in range(10000)]
num_list = [int(x) for x in input().split()]
for i in num_list:
    t = i
    while(t!=1):
        if(t%2==1):
            t=t*3+1
        t=t//2
        if(now_list[t]==1):
            break
        now_list[t]=1
num_list.sort(reverse=True)
flag = 0
for i in num_list:
    if(now_list[i]==0):
        if(flag==1):
            print(' ',end='')
        print(i,end='')
        flag=1
print()
