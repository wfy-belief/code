# 两短边之和大于长边即可
a, b, c = map(int, input().split())
# if max(a, b, c) > a + b + c - max(a, b, c)
if 2 * max(a, b, c) < a + b + c:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'area = {area:.2f}; perimeter = {s * 2:.2f}')
else:
    print('These sides do not correspond to a valid triangle')
