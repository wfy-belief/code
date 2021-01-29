def find_point(n_):
    for i in range(n_):
        for j in range(n_):
            if map_[i][j] == max(map_[i]) and map_[i][j] == min([map_[k][j] for k in range(n_)]):
                return i, j
    return ('NONE',)


n = int(input())
map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split())))
print(*find_point(n))
