t, k = map(int, input().split())
for i in range(k):
    l = [int(x) for x in input().split()]
    if l[2] > t:
        print('Not enough tokens.  Total = %d.' % t)
    else:
        if l[0] < l[3]:
            if l[1] == 1:
                t += l[2]
                print('Win %d!  Total = %d.' % (l[2], t))
            else:
                t -= l[2]
                print('Lose %d.  Total = %d.' % (l[2], t))
        else:
            if l[1] == 1:
                t -= l[2]
                print('Lose %d.  Total = %d.' % (l[2], t))
            else:
                t += l[2]
                print('Win %d!  Total = %d.' % (l[2], t))
        if t <= 0:
            print('Game Over.')
            break
