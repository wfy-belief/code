import heapq

# list 转换为 heap
from typing import List

l: List[int] = [1, 2, 3, 4, 5]
heapq.heapify(l)
# 入队
heapq.heappush(l, 6)
# 出队
print(heapq.heappop(l))
# 取前n大元素
print(heapq.nlargest(3, l))
print(l)
# 合并堆
ll = [-1, -2, -3, -4]
print(list(heapq.merge(ll, l)))


# 优先队列
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f'{self.name} {self.age}'


person = [Person('a', 3), Person('b', 5), Person('c', 4)]
heapq.heapify(person)
print(heapq.heappop(person))
