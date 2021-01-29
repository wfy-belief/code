# 分子 1 2 3 = i + 1
# 分母 1 3 5 = 2 * i + 1
# 符号 = -1 ** i
n = int(input())
ans = 0
for i in range(n):
    ans += ((-1) ** i) * (i + 1) / (2 * i + 1)
print(f'{ans:.3f}')
