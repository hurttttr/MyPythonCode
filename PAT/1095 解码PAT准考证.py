n = input().split()
ans = []
for i in range(int(n[1])):
    tmp = input().split()
    tmp[0] = float(tmp[0])
    ans.append(tmp)

l = ['a', 'b', 'c', 'd', 'e']
wrong = {}

for i in range(int(n[0])):
    stu = []
    score = 0.0
    m = input()[1:-1].split(') (')  # 分离
    for x in m:
        stu.append(x.split())
    for j in range(int(n[1])):
        stu_l = stu[j][1:]  # 学生答案
        ans_l = ans[j][3:]  # 正确答案
        for a in l:
            if a in stu_l and a in ans_l:  # 移除两者的交集
                stu_l.remove(a)
                ans_l.remove(a)
        if not stu_l and not ans_l:  # 两者为空，全对
            score += ans[j][0]
        elif not stu_l and ans_l:  # 学生答案为空，部分正确
            score += ans[j][0] / 2
        if stu_l:
            for k in stu_l:
                if (j + 1, k) in wrong.keys():  # 元组作为key，标识题号和选项
                    wrong[(j + 1, k)] += 1
                else:
                    wrong[(j + 1, k)] = 1
        if ans_l:
            for k in ans_l:
                if (j + 1, k) in wrong.keys():
                    wrong[(j + 1, k)] += 1
                else:
                    wrong[(j + 1, k)] = 1
    print(score)
if not wrong:
    print("Too simple")
else:
    maxx = max(wrong.values())
    rst = []
    for k, v in wrong.items():
        if v == maxx:
            rst.append(k)
    rst.sort(key=lambda x: x[1])
    rst.sort(key=lambda x: x[0])
    for i in rst:
        print('{} {}-{}'.format(maxx, i[0], i[1]))
