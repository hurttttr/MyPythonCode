import math
a = int(input())
b = [int(i) for i in input().split()]
if a==1:
    print(b[0],end="")
else:
    b.sort(reverse = True)
    b=list(map(str,b))
    if math.sqrt(a)%1==0:
        m=int(math.sqrt(a))
    else:
        m =int(math.sqrt(a)+1)
    while a%m!=0:
        m+=1
    n = a//m
    matrix = [[0 for i in range(n)] for i in range(m)]
    k = 0
    i = 0
    j = 0
    l = 0
    while k<a:
        while k<a and i<n-1:
            matrix[j][i]=b[k]
            i+=1
            k+=1
        while k<a and j<m-1:
            matrix[j][i]=b[k]
            j+=1
            k+=1
        while k<a and i>l:
            matrix[j][i]=b[k]
            i-=1
            k+=1
        while k<a and j>l:
            matrix[j][i]=b[k]
            j-=1
            k+=1
        i,j,l,m,n=i+1,j+1,l+1,m-1,n-1
        if k==a-1:                    
            matrix[j][i]=b[k]
            k+=1
    for i in matrix:
        print(" ".join(i))