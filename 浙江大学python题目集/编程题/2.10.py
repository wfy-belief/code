lower, upper = map(int, input().split())
print("Invalid." if lower > upper else "fahr celsius")
for i in range(lower, upper + 1, 2):
    c = 5 * (i - 32) / 9
    print(f'{i}{c:>6.1f}')
