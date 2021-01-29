# 自然数列 11 - m
m = int(input())
# 等差数列的和=(首数+尾数)*项数/2
ans = (11 + m) * (m - 11 + 1) // 2
print(f'sum = {ans}')