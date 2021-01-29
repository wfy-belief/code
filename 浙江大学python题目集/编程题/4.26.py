import math

n = int(input())
print("n={},s={}".format(n, sum([math.factorial(i) for i in range(1, n + 1, 2)])))
