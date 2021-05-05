N = int(input())
for i in range(N):
    t = input()
    if len(t) < 6:
        print('Your password is tai duan le.')
        continue
    else:
        a, b = 0, 0
        for j in t:
            if j.isdigit():
                a += 1
            elif j.isalpha():
                b += 1
            elif j != '.':
                print('Your password is tai luan le.')
                break
        else:
            if a > 0 and b > 0:
                print('Your password is wan mei.')
            elif a > 0:
                print('Your password needs zi mu.')
            elif b > 0:
                print('Your password needs shu zi.')
            continue
