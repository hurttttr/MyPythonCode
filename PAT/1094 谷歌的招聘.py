L, K = map(int, input().split())
N = input()
for i in range(L-K+1):
    t = N[i:i+K]
    int_t = int(t)
    if int_t == 2:
        print(t)
        break
    elif int_t == 1 or int_t % 2 == 0 or int_t == 0:
        continue
    else:
        for j in range(3, int(int_t**0.5)+2, 2):
            if int_t % j == 0:
                break
        else:
            print(t)
            break
else:
    print('404')
