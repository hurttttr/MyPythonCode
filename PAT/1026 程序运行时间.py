a, b = map(int, input().split())
s = (b-a+50)//100
t = s % 60
h = s // 3600
m = s // 60 - h*60
print('%02d:%02d:%02d' % (h, m, t))
