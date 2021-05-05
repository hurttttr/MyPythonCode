import time


ticks1 = time.time()

t1 = ['0']*100000
for i in range(100000):
    t1[i] = i

ticks2 = time.time()

t2 = []
for i in range(100000):
    t2.append(i)

ticks3 = time.time()

print(ticks2-ticks1)
print(ticks3-ticks2)
