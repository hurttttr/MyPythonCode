import string

with open("hamlet.txt",'r') as f:
    txt = f.read().lower()

for i in string.punctuation:
    txt = txt.replace(i,' ')
excepts = ['the','to','you','and','my','in','of','is','at','it','not','his','but','for',]
for i in excepts:
    txt = txt.replace(i,' ')

txt = txt.split()
dic = {}
for i in txt:
    if len(i)>1:
        dic[i] = dic.get(i,0)+1

lst = sorted(dic.items(),key=lambda x : -x[1])
for i in range(10):
    print('{:<10}{:>5}'.format(lst[i][0],lst[i][1]))