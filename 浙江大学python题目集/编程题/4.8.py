# 比较简单 题解来源于网络
n = int(input())
a, b = 1, 2
result = 0
for i in range(0, n):
    result = result + b / a
    a, b = b, a + b
print("{:.2f}".format(result))
