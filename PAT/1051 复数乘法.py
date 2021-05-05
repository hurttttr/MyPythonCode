import math

R1, P1, R2, P2 = map(eval, input().split())
A = R1*R2*math.cos(P1)*math.cos(P2)-R1*R2*math.sin(P1)*math.sin(P2)
B = R1*R2*math.cos(P1)*math.sin(P2)+R2*R1*math.sin(P1)*math.cos(P2)
if -0.005 <= A < 0:
    print('0.00', end='')
else:
    print('%.2f' % A, end='')
if B >= 0:
    print('+%.2fi' % B)
elif -0.005 <= B < 0:
    print('+0.00i')
else:
    print('%.2fi' % B)
