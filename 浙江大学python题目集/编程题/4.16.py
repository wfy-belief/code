a, b, c = map(int, input().split())
if 2 * max(a, b, c) < a + b + c:
    print('yes')
else:
    print('no')
