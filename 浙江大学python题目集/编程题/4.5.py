mul_ = 1
ans = 1
n = int(input())
for i in range(1, n + 1):
    mul_ *= i
    ans += 1 / mul_
print(f'{ans:.8f}')
