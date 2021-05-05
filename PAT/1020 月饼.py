n, m = map(int, input().split())
l = [float(x) for x in input().split()]
price = [float(x) for x in input().split()]
ave = [[l[i], price[i], price[i]/l[i]] for i in range(n)]
ave.sort(key=lambda x: -x[2])
ans = 0
for i in ave:
    if m > i[0]:
        m -= i[0]
        ans += i[1]
    else:
        ans += m*i[2]
        break
print('%.2f' % ans)
