m, n = map(int, input().split())
ans = 0.0
for i in range(m, n + 1):
    ans += i ** 2 + 1 / i
print(f'sum = {ans:.6f}')
