n = input()
conutt = n.count('T')
countp = 0
countsum = 0
for i in n:
    if i == 'P':
        countp += 1
    elif i == 'T':
        conutt -= 1
    else:
        countsum = (countsum+conutt*countp) % 1000000007
print(countsum)
