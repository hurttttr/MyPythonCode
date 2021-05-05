n = int(input())
student = [[x for x in input().split()] for i in range(n)]
max = ['','',0]
min = ['','',100]
for i in student:
    if(int(i[2])>int(max[2])):
        max=i
    if(int(i[2])<int(min[2])):
        min=i
print(max[0]+' '+max[1])
print(min[0]+' '+min[1])