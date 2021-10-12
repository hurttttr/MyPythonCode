import sys
def main():
    address,n,k=sys.stdin.readline().split()
    n=int(n)
    k=int(k)
    #记录结点的信息
    dic={}
    for i in range(n):
        addr,data,next=sys.stdin.readline().split()
        dic[addr]=(addr,data,next)


    lst_1=[]
    lst_2=[]
    lst_3=[]

    while address!="-1":
        l1=dic[address]
        if int(l1[1])<0:
            lst_1.append((l1[0],l1[1]))
        elif int(l1[1])<=k:
            lst_2.append((l1[0],l1[1]))
        else:
            lst_3.append((l1[0],l1[1]))
        address=l1[2]
    # lst_2=[]

    lst_1.extend(lst_2)
    lst_1.extend(lst_3)


    for i in range(len(lst_1)-1):
        sys.stdout.write(f"{lst_1[i][0]} {lst_1[i][1]} {lst_1[i+1][0]}\n")
    sys.stdout.write(f"{lst_1[-1][0]} {lst_1[-1][1]} {-1}\n")


main()
