from collections import Counter

l = list(map(int, input().split()))
l.pop(0)
cnt = Counter(l)
print(*cnt.most_common(1)[0])

#
ans = max(set(l), key=l.count)
print(ans, l.count(ans))
