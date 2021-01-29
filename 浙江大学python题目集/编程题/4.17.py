import math

n = int(input())
for i in range(int(math.pow(10, n - 1)), int(math.pow(10, n))):
    sum_ = 0
    j = i
    while j >= 1:
        sum_ = sum_ + math.pow(j % 10, n)
        j = j // 10
    if sum_ == i:
        print('{:d}'.format(i))
