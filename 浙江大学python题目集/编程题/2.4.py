a, n = input().split()
ans = 0
for i in range(1, int(n) + 1):
    ans += int(a * i)
print(f's = {ans}')