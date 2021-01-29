n = int(input())
ans = ''
for _ in range(n):
    s = input()
    ans = max(ans, s, key=len)
print(f'The longest is: {ans}')
