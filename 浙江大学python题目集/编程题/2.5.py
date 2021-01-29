# an = 2 * n - 1 or 2 * n + 1
n = int(input())
ans = 0
for i in range(n):
    ans += 1 / (2 * i + 1)
print(f'sum = {ans:.6f}')
