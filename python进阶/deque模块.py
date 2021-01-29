from collections import deque

# 双端队列
# 队列，典型的数据类型结构，先进先出
# 入队
d = deque((1, 2, 3))
print(d)
d.append(4)
d.appendleft(0)
print(d)
# 出队
d.pop()
d.popleft()
print(d)

# extend
d.extend((4, 5, 6))
d.extendleft((-2, -1, 0))
print(d)
