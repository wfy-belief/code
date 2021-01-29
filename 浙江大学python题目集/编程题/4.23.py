n, m = map(int, input().split())
map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split())))
ans_ = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if map_[i][j] > max(map_[i - 1][j], map_[i + 1][j], map_[i][j - 1], map_[i][j + 1]):
            ans_.append((map_[i][j], i + 1, j + 1))
if not ans_:
    print('None', n, m)
for item in ans_:
    print(*item)
