T = int(input())
for i in range(1,T+1):
    a, b, c = map(float,input().split())
    if(a+b>c):
        print('Case #'+str(i)+': true')
    else:
        print('Case #'+str(i)+': false')