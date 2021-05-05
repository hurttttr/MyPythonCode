n = int(input())
scorelst = [0]*10000
for i in range(n):
    num, score = map(str, input().split())
    dnum, ynum = map(int, num.split('-'))
    scorelst[dnum] += int(score)
print(scorelst.index(max(scorelst)), max(scorelst))
