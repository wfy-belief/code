ans = 1
n = int(input())
for _ in range(n - 1):
    # 3 1 + 1  = ans
    ans = (ans + 1) * 2
print(ans)
