n = eval(input())

dit = {}  # 存入数据
for i in range(n):
    s = input().split()
    # 加权
    if s[0][0] == "A":
        score = int(s[1])
    if s[0][0] == "B":
        score = int(s[1])/1.5
    if s[0][0] == "T":
        score = int(s[1])*1.5

    school = s[2].lower()
    if school not in dit:
        dit[school] = dit.get(school, [0, 0])  # 这句收获贼大，原先没有想到用get()处理字典中存入数据
        dit_list = dit[school]  # 感觉好神奇
        dit_list[0] = score
        dit_list[1] = 1
    else:
        dit_list = dit[school]
        dit_list[0] += score
        dit_list[1] += 1

res_list = []  # 放到数组中再排序，节省操作，妙
for k, v in dit.items():
    res_list.append([k, int(v[0]), v[1]])
res_list = sorted(res_list, key=lambda x: (-x[1], x[2], x[0]))  # 有的升序，有的降序

print(len(dit))
con = 1
s = res_list[0][1]  # 用于存储排名
for i in range(len(res_list)):
    if s != res_list[i][1]:
        con = i+1  # 不是con+=1而是con=i+1解决并列问题
    print("%d %s %d %s" %
          (con, res_list[i][0], res_list[i][1], res_list[i][2]))
    s = res_list[i][1]

'''
import sys

N = int(input())
dic = {}
school_set = set()
for i in range(N):
    z, grade, s = sys.stdin.readline().split()
    grade, s = int(grade), s.lower()
    if z[0] == 'B':
        t = int(grade/1.5)
    elif z[0] == 'A':
        t = grade
    else:
        t = int(grade*1.5)
    if s in school_set:
        dic[s][0] += t
        dic[s][1] += 1
    else:
        school_set.add(s)
        dic[s] = [t, 1]
lst = []
for i, j in dic.items():
    lst.append([i, j[0], j[1]])
lst.sort(key=lambda x: (-x[1], x[2], x[0]))
print(len(lst))
current_grade, index = 0, 1
for i, j in enumerate(lst, start=1):
    if j[1] < current_grade:
        index = i
    sys.stdout.writelines('{} {} {} {}\n'.format(
        index, j[0], j[1], j[2]))
    current_grade = j[1]

'''
