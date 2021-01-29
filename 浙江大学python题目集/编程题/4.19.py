n = int(input())
l = []
for _ in range(n):
    line = list(map(int, input().split()))
    l.append(line)
ans = 0
for j in range(n):
    for k in range(n):
        if j != n - 1 and k != n - 1 and j + k != n - 1:
            ans += l[j][k]
print(ans)
