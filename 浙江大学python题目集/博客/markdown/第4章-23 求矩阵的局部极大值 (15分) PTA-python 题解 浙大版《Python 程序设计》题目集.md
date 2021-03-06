
> 致读者： 博主是一名数据科学与大数据专业大三的学生，一个互联网新人，这篇文章是记录我作为python助教总结的简单题解，**<font color='#e59572'>写博客一方面是为了记录自己的学习过程中遇到的问题和思考，一方面是希望能够帮助到很多和自己一样处于困惑的读者。</font>**
> 由于水平有限，博客中难免会有一些错误，有纰漏之处恳请各位大佬不吝赐教！之后会写大数据专业的文章哦。
> GitHub链接[https://github.com/wfy-belief](https://github.com/wfy-belief)
> **<font color='#e59572'>尽管现在我的水平可能还不太及格，但我会尽我自己所能，做到最好☺</font>**。——天地有正气，杂然赋流形。下则为河岳，上则为日星。
---
# 求矩阵的局部极大值
给定$$M$$行$$N$$列的整数矩阵$$A$$，如果$$A$$的非边界元素$$A[i][j]$$大于相邻的上下左右4个元素，那么就称元素$$A[i][j]$$是矩阵的局部极大值。本题要求给定矩阵的全部局部极大值及其所在的位置。

### 输入格式：

输入在第一行中给出矩阵$$A$$的行数$$M$$和列数$$N$$（$$3\le M, N\le 20$$）；最后$$M$$行，每行给出$$A$$在该行的$$N$$个元素的值。数字间以空格分隔。

### 输出格式：

每行按照“元素值 行号 列号”的格式输出一个局部极大值，其中行、列编号从1开始。要求按照行号递增输出；若同行有超过1个局部极大值，则该行按列号递增输出。若没有局部极大值，则输出“None 总行数 总列数”。

### 输入样例1：
```in
4 5
1 1 1 1 1
1 3 9 3 1
1 5 3 5 1
1 1 1 1 1
```

### 输出样例1：
```out
9 2 3
5 3 2
5 3 4
```

### 输入样例2：
```
3 5
1 1 1 1 1
9 3 9 9 1
1 5 3 5 1
```

### 输出样例2：
```
None 3 5
```
### 思路与视频教程
**<font color='#e59572'>慢慢完善</font>**

### 代码
```python
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

```