single = ['', 'jan', 'feb', 'mar', 'apr', 'may',
          'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
tens = ['', 'tam', 'hel', 'maa', 'huh', 'tou',
        'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']

n = int(input())
for i in range(n):
    s = input()
    try:
        s = int(s)
        if s == 0:
            print('tret')
            continue
        a = s % 13  # 个位数
        b = s // 13  # 十位数
        if a == 0 or b == 0:
            rst = tens[b] + single[a]
        else:
            rst = tens[b] + ' ' + single[a]
        print(rst)

    except:
        rst = 0
        s = s.split()
        for j in s:
            if j in single:
                rst += single.index(j)
            elif j in tens:
                rst += tens.index(j) * 13
        print(rst)
