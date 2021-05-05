n = int(input())
for i in range(n):
    s = input()
    f=0
    l = len(s)
    if(l<3):
        print('NO')
        continue
    for i in s:
        if(i!='P' and i!='T' and i!='A'):
            print('NO')
            f=1
            break
    if(f==1):
        continue
    P_stn = s.index('P')
    T_stn = s.index('T')
    if(T_stn-P_stn-1==0):
        print('NO')
    else:
        if(P_stn*(T_stn-P_stn-1)==l-T_stn-1):
            print('YES')
        else:
            print('NO')