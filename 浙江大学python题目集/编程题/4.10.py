from math import gcd
m, n = map(int, input().split())
ans = gcd(m, n)
print(ans, m * n // ans)
