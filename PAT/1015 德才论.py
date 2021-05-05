def fun(x):
    sum = -int(x[1])-int(x[2])
    a = -int(x[1])
    b = x[0]
    return sum, a, b


N, L, H = map(int, input().split())
student = []
s1 = []
s2 = []
s3 = []
s4 = []
for i in range(N):
    student.append(input().split())
    if int(student[i][1]) >= 80 and int(student[i][2]) >= 80:
        s1.append(student[i])
    elif int(student[i][1]) >= 80 and int(student[i][2]) >= 60 and int(student[i][2]) < 80:
        s2.append(student[i])
    elif int(student[i][1]) >= 60 and int(student[i][2]) >= 60 and int(student[i][1]) > int(student[i][2]):
        s3.append(student[i])
    elif int(student[i][1]) >= 60 and int(student[i][2]) >= 60:
        s4.append(student[i])
s1.sort(key=fun)
s2.sort(key=fun)
s3.sort(key=fun)
s4.sort(key=fun)
s = s1+s2+s3+s4
print(len(s))
for i in s:
    print(' '.join(i))


# https://www.pythonf.cn/read/58505
