from functools import reduce
s = input()
ans = reduce(lambda x, y: int(x) + int(y), s)
print(len(s), ans)
