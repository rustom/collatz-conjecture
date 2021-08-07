def nextNumber(n):
    if n % 2: 
        return 3 * n + 1 
    else:
       return n / 2

ntries = 1000000
tries = []

for i in range(1, ntries): 
    temp = i
    count = 0
    while temp != 1: 
        temp = nextNumber(temp)
        count += 1
    print(i, 'took', count, 'tries to reach 1')
    tries.append(count)
    count = 0

print(tries.index(max(tries)), 'took', max(tries), 'tries')
