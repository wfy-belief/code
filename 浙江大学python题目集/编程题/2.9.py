from typing import List

l: List[int] = list(map(int, input().split()))  # 转换为int类型的列表
l.sort()  # 排序
print(*l, sep='->')
