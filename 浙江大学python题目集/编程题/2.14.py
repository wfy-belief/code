# 感谢XX朋友供稿
def field(m, n):
    ans, k = 0, 0
    for i in range(m, n + 1):
        ans += i
        k += 1
        print(f'{i:>5d}', end="")
        if k % 5 == 0 or i == n:
            print()
    print(f'Sum = {ans}')


m, n = map(int, input().split())
field(m, n)
