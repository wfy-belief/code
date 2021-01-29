# 这个题目不是太难 代码来源于网络
n = int(input())
if n == 0:
    print("Invalid.")
else:
    a = 1
    b = 1
    for i in range(0, n):
        print("{:>11d}".format(a), end="")
        a, b = b, a + b
        if i % 5 == 4:
            print()
